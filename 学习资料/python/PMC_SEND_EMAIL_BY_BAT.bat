@echo off
set script_path=D:\tongyong_project\MMS_AUTO_TEST\AutomationTest\PMC\测试场景
set report_path=D:/PMC_TEST_REPORT测试场景

echo ======
echo 进入目录
echo.
setlocal enabledelayedexpansion 
for /l %%i in (1,1,10) do (jmeter -n -t D:\PMC_AUTO_TEST_BAT\script\pmc.jmx -l D:\test\jtl\%%i.jtl -e -o D:\test\html_report\HTML_Report%%i ping 127.0.0.01 -n 5)

 @echo off
set script_path=D:\PMC_AUTO_TEST_BAT\script\
set file_name=%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%
set "file_name=%file_name: =0%"
md D:\test\jtl
md D:\test\html_report\%file_name%

D:
cd %script_path% 
@echo %file_name%




cmd /k cd /d %script_path% 

echo "pabot --processes 1 --outputdir D:/PMC_TEST_REPORT/back_1 2019_10_24_回归测试.robot"

endlocal
pause
@echo jmeter -n -t D:\PMC_AUTO_TEST_BAT\script\pmc.jmx -l D:\test\jtl\%file_name%.jtl -e -o D:\test\html_report\HTML_Report
