@echo off
::jmeter脚本的路径
set script_path=D:\PMC_AUTO_TEST_BAT\script\
:: 年月日，时分秒
set file_name=%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%
:: 7z安装路径
set zip7= C:\Program Files\7-Zip\7z.exe
:: 当前日期，备份文件名 年月日
set curdate=%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%
:: 设置压缩包保存路径 
set save=D:\test\html_report
::设置要打包压缩的文件夹  注意 set filename= 赋值时，不能有空格，等号两边不能空格.
set will_pack=D:\test\html_report\HTML_Report_01
:: 压缩脚本生成的报告
7z a -tzip %save%\%curdate%.zip %will_pack% -mx0 -xr!.svn

set from=13122395209@163.com
set user=13122395209
set pass=Aa12341234K@
set to=639223264@qq.com
set subject= 促销-%curdate%-测试报告
set mail=这个试试哈
set attach="%save%\%curdate%.zip"
set server=smtp.163.com
set debug=-debug -log blat.log -timestamp

echo %attach%

blat %mail% -to %to% -base64 -charset Gb2312 -subject %subject% -attach %attach% -server %server% -f %from% -u %user% -pw %pass% %bug%

pause


blat C:/mail.txt -to demo@demo.com -attach "C:/fujia.txt" -s "zhuti" -u user@163.com -pw password -charset Gb2312
blat D:/test/html_report/20200918153354.zip -to 639223264@qq.com -attach "D:/test/html_report/20200918153354.zip" -s "Test0001" -u 13122395209@163.com -pw Aa12341234K@ -charset Gb2312


