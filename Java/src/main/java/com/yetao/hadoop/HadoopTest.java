package com.yetao.hadoop;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.OutputStream;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.FileUtil;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;

import javax.security.auth.login.AppConfigurationEntry;

public class HadoopTest {


    public static Configuration conf = null;
    static {
        conf = new Configuration() {
            public AppConfigurationEntry[] getAppConfigurationEntry(String name) {
                return new AppConfigurationEntry[0];
            }
        };
        conf.set("fs.defaultFS", "hdfs://192.168.20.101:9000");
    }

    // 列表
    public static void ls(String pathStr) throws Exception {
        FileSystem fs = FileSystem.get(conf);
        Path path = new Path(pathStr);
        FileStatus[] status = fs.listStatus(path);
        Path[] listPaths = FileUtil.stat2Paths(status);
        for (Path p : listPaths) {
            System.out.println(p); // 循环打印目录结构
        }
    }

    // 创建文件夹
    public static boolean mkdir(String path) throws Exception {
        FileSystem fs = FileSystem.get(conf);
        Path pa = new Path(path);
        if (!fs.exists(pa)) {
            fs.mkdirs(pa);
            return true;
        } else {
            return false;
        }
    }

    public static void uploadFile(String sourceFile, String targetDir, String fileName) throws Exception {
        FileSystem fs = FileSystem.get(conf);
        Path target = new Path(targetDir + "/" + fileName);
        OutputStream out = fs.create(target);
        InputStream in = new FileInputStream(new File(sourceFile + "/" + fileName));
        IOUtils.copyBytes(in, out, 4096, true);
    }

    public static void main(String[] args) throws Exception {
        HadoopTest.ls("/firstDay/temp");
    }
}
