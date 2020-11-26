@echo off
:: blatt安装目录
set _extendDir=D:\PMC_AUTO_TEST_BAT\script\
D:
cd  %_extendDir%
:: 设置消息
:: 标题
set s="chnnel tomcat is restart"
:: 正文内容，采用文本预先编辑好，会显示到邮件正文部分
set mail=%_extendDir%\jmeter.log
:: 接收人
set t=639223264@qq.com
:: 发送人
set f=13122395209@163.com
:: 163邮件服务器授权码
set pw=Aa12341234K@
:: 发送消息
echo %mail%
blat %mail% -s %s% -to %t% -server smtp.163.com -f %f% -u %f% -pw %pw%
pause
