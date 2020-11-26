package com.yetao.hbase;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.client.*;
import org.apache.hadoop.hbase.util.Bytes;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class HbaseTest {

    private static Configuration conf;

    private static Connection con;

    static {
        conf = HBaseConfiguration.create();
        conf.set("hbase.zookeeper.quorum","192.168.20.101");
        conf.set("hbase.zookeeper.property.clientPort","2181");
        try {
            con = ConnectionFactory.createConnection(conf);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public byte[] obj2Byte(Object obj) throws Exception {
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(bos);
        oos.writeObject(obj);
        return bos.toByteArray();
    }

    public Object byte2Obj(byte[] bytes) throws Exception{
        Object obj;
        ByteArrayInputStream bis = new ByteArrayInputStream(bytes);
        ObjectInputStream ois = new ObjectInputStream(bis);
        obj = ois.readObject();
        return obj;
    }

    public void putMessage(String tableName,String rowName,String family,String cellName,Object value) throws Exception {
        Table table = getCon().getTable(TableName.valueOf(tableName));
        Put put = new Put(rowName.getBytes());
        byte[] bs =obj2Byte(value);
        put.addColumn(family.getBytes(),cellName.getBytes(),bs);
        table.put(put);
    }

    public String getMessage(String tableName,String rowName,String family,String cellName) throws Exception{
        Table table = getCon().getTable(TableName.valueOf(tableName));
        Result result = table.get(new Get(rowName.getBytes()));
        System.out.println(result);
        byte[] bs = result.getValue(family.getBytes(),cellName.getBytes());
        String rs = (String) byte2Obj(bs);
        return rs;
    }

    //新增表
    public boolean createTable(String tableName,String... columnFamilys) throws Exception {
        Connection conn = getCon();
        Admin admin = conn.getAdmin();
        TableName tn = TableName.valueOf(tableName);
        boolean exists = admin.tableExists(tn);
        if (exists){
            return false;
        }
        TableDescriptorBuilder tdb = TableDescriptorBuilder.newBuilder(tn);
        List<ColumnFamilyDescriptor> cfs = new ArrayList<ColumnFamilyDescriptor>();
        for(String columnFamily:columnFamilys){
            ColumnFamilyDescriptor cf = ColumnFamilyDescriptorBuilder.newBuilder(columnFamily.getBytes()).build();
            cfs.add(cf);
        }
        tdb.setColumnFamilies(cfs);
        admin.createTable(tdb.build());
        return false;
    }

    public static Connection getCon(){
        if(con==null){
            try {
                con = ConnectionFactory.createConnection(conf);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return con;
    }
    public static void main(String[] args) throws Exception {
        //boolean suucess = new HbaseTest().createTable("test_javaapi", "s1", "s2");
        //new HbaseTest().putMessage("test_javaapi","100001","name","n1","张三");
        String message = new HbaseTest().getMessage("test_javaapi", "100001", "name", "n1");
        System.out.println(message);
        //System.out.println(suucess);
//        byte[] bs = new HbaseTest().obj2Byte("你好");
//        String localChartSet = System.getProperty("file.encoding");
//        System.out.println("localChartSet>>>>"+localChartSet);
//        for(byte b:bs){
//            System.out.print(b);
//        }
//        bs = "你好".getBytes();
//
//        System.out.println("");
//        for(byte b:bs){
//            System.out.print(b);
//        }
    }

}
