https://mazhuang.org/awesome-adb
adb 学习网站

Android 夜神模拟器 + appium + pytest + allure 测试框架搭建
1,Java jdk 安装
      查看java版本： 运行 > cmd > java -version
2.下载Android adk 

   链接：http://tools.android-studio.org/index.php/sdk

   版本：installer_r24.4.1-windows.exe(Recommended)
3.安装sdk

以管理员身份运行（个人习惯操作，你也可以通过打开安装），一路next，

注意：一定要记住安装路径，因为配置环境变量要用

4.配置环境变量
  1）新增系统变量

         SDK = D:\installed\android_sdk (根据自己实际路径填写）
  2）编辑path

         在path的最后增加 ;%SDK%\platform-tools;%SDK%\tools
注意： 
    a.记住一定是在path变量的后面增加，千万不要将path原有的内容给误删了
    b.如果原有的path最后有一个分号，那么，第一个%SDK%前分号就不要写了，即只写%SDK%\platform-tools;%SDK%\tools
a5.通过android sdk manager安装包（通过android_sdk安装包下的SDK Manager.exe打开

6.安装node
     链接：https://nodejs.org/en/download/

7,安装appiumserver + appium 客户端
    
    7.1、安装appium-desktop.exe 设置默认端口：127.0.0.1:4723
    7.2、安装node.js 并配置环境变量，检查是否安装成功：node -v 或 npm
    7.3、安装cnpm（使用淘宝镜像） 为了安装appium服务端+客户端所用
    npm install -g cnpm --registry-https://registry.npm.taobao.org
    7.4、安装appium cnpm install -g appium  --配置环境变量 appium_home
    7.5、安装appium-python-client pip3 install Appium-Python-Client
    报错：error:invalid command ‘egg_info’
    7.6  appium-doctor 检查是否环境安装成功

1.背景：测试京东APP时点击截图，第一张没问题，第二张截图报下面的错误。
Error while obtaining UI hierarchy XML file: com.android.ddmlib.SyncException: Remote object doesn't exist!

解决办法1： 写个脚本跑 
#!/bin/sh
builddate=`date '+%Y%m%d%H%M'`
adb shell uiautomator dump /sdcard/app.uix
adb pull /sdcard/app.uix ./app${builddate}.uix
#存到E盘的app.uix文件中，在E盘新建一个文本文档改成app.uix
adb shell screencap -p /sdcard/app.png
adb pull /sdcard/app.png ./app${builddate}.png

问题解决办法2：

方法一：直接插拔USB，然后重新连接，一般都会好

方法二：在命令窗口中将adb kill掉，输入：adb kill-server，然后重新运行uiautomatorviewer命令打开窗口连接，一般也会好

PS 具体：Android这边需要看源码。解释出为什么截图后面不可以正常运行


https://github.com/appium/appium-desktop/releases/download/v1.19.1/Appium-1.19.1-mac.zip

问题1：Android ADB 命令+ 夜神模拟器  = 测试 Android手机自动化
1,下载Adb 
2,将Adb.exe 替换到 夜神模拟器安装目录的bin目录下，
将夜神的 nox_adb.exe(旧)修改成 nox_adb_bak.exe,
将自身下载并配置到环境变量的ADB.exe Copy放入夜神模拟器bin目录中，并改成名称为nox_adb.exe

问题2： appium 测试android机器 selenium.common.exceptions import InvalidArgumentException--ImportError: cannot import name 'InvalidArgumentException'
    Python路径\Lib\site-packages\selenium\common找到exceptions.py添加下面这个类就行了
    class InvalidArgumentException(WebDriverException):
        pass
问题3：appium===报错Failure [INSTALL_FAILED_ALREADY_EXISTS: Attempt to re-install io.appium.settings without first uninstalling.的解决办法
    解决方案地址：https://blog.csdn.net/pjl6523853/article/details/72886048

问题4： adb devices 出现 连接不上设备问题，很有可能是 电脑有两个adb.exe程序再跑

问题5：adb 命令 + appium连接手机命令一起时，会导致adb 连接不上的问题，可以选择重新启动手机
     
adb 无线连接手机：
1.先通过USB连接手机，使用adb devices命令，查看连接是否正常
2.查看IP，adb shell ifconfig wlan0；或者直接在“手机-设置”里面查看:adb connect 10.49.110.183
3.通过Adb tcpip 5555命令，重启tcpip，并监听5555端口
4.输入adb connect 192.168.. (手机ip地址）命令，直到出现connected to XXX，如果不行，拔掉USB线，多试几次
5.此时就可以通过WiFi执行adb命令了
Chrome浏览器中有一个发送adb命令的插件，安装插件的方法自己百度。安装完后，打开Chrome ADB，自动就可以连接上，
进行操控了（左侧栏，device下面显示的就是ip地址和端口号）

注意点：
1.先确保你手机和电脑运行在同一wifi局域网内，手机不需要root
2.由于是通过adb来进行连接的，所以确保你配置了环境变量
3.第一次的时候需要用手机USB连接到你的电脑

adb-monkey 解答
adb monkey
一、 什么是Monkey
Monkey是Android中的一个命令行工具，可以运行在模拟器里或实际设备中。它向系统发送伪随机的用户事件流(如按键输入、触摸屏输入、手势输入等)，实现对正在开发的应用程序进行压力测试。Monkey测试是一种为了测试软件的稳定性、健壮性的快速有效的方法。

二、 Monkey的特征
1、 测试的对象仅为应用程序包，有一定的局限性。
2、 Monkey测试使用的事件流数据流是随机的，不能进行自定义。
3、 可对MonkeyTest的对象，事件数量，类型，频率等进行设置。

三、Monkey的基本用法
基本语法如下：
$ adb shell monkey [options]
如果不指定options，Monkey将以无反馈模式启动，并把事件任意发送到安装在目标环境中的全部包。下面是一个更为典型的命令行示例，它启动指定的应用程序，并向其发送500个伪随机事件：
$ adb shell monkey -p your.package.name -v 500
adb shell monkey -p com.amaker.mp -v 500
adb shell monkey -p com.amaker.mp -v 500 > c:\monkeya.txt
四、Monkey测试的一个实例
通过这个实例，我们能理解Monkey测试的步骤以及如何知道哪些应用程序能够用Monkey进行测试。
Windows下（注：2—4步是为了查看我们可以测试哪些应用程序包，可省略）：
1、 通过eclipse启动一个Android的emulator
2、 在命令行中输入：adb devices查看设备连接情况
adb devices
3、 在有设备连接的前提下，在命令行中输入：adb shell 进入shell界面
C:\Documents and Settings\Administrator>adb shell

4、 查看data/data文件夹下的应用程序包。注：我们能测试的应用程序包都在这个目录下面
C:\Documents and Settings\Administrator>adb shell

ls data/data

ls data/data

5、 以com.amaker.mp作为对象进行MonkeyTest
#monkey -p com.amaker.mp -v 500
其中-p表示对象包 –v 表示反馈信息级别
运行过程中，Emulator中的应用程序在不断地切换画面。
按照选定的不同级别的反馈信息，在Monkey中还可以看到其执行过程报告和生成的事件。

Monkey参数分析
-p： 被测试app的包名，
设置事件百分比,所有的百分比加起来不能超过100%
0：触摸事件百分比，即参数–pct-touch
1：滑动事件百分比，即参数–pct-motion
2：缩放事件百分比，即参数–pct-pinchzoom
5：轨迹球事件百分比，即参数–pct-trackball
4：屏幕旋转事件百分比，即参数–pct-rotation
3：基本导航事件百分比，即参数–pct-nav
6：主要导航事件百分比，即参数–pct-majornav
7：系统事件百分比，即参数–pct-syskeys
8：Activity启动事件百分比，即参数–pct-appswitch
9：键盘翻转事件百分比，即参数–pct-flip
10：其他事件百分比，即参数–pct-anyevent
–throttle 300：在事件之间插入固定的时间（毫秒）延迟，你可以使用这个设置来减缓Monkey的运行速度，如果不指定参数，则事件之间将没有延迟，
事件将以最快的速度生成
–throttle time --randomize-throttle 设置随机时间的时间间隔区间[随机时间]
例：adb shell monkey 100 --throttle 500 --randomize-throttle
说明：执行一百次monkey随机事件，每次事件的间隔在0到500毫秒之间不固定
–ignore-crashes：忽略程序崩溃，设置此选项后，Monkey会执行完所有的事件，不会因crash而停止。
–ignore-timeouts：忽略程序无响应，设置此选项后，Monkey会执行完所有的事件，不会因ANR而停止
–ignore-native-crashes 忽略monkey本身的异常，直到事件执行完毕
例：adb shell monkey --ignore-native-crashes -v 100
–ignore-security-exceptions：忽略证书或认证异常，设置此选项后，Monkey会执行完所有的事件，不会因认证或证书异常而停止
–monitor-native-crashes：监视系统中本地代码发生的崩溃
-v -v -v：每个-v都将增加反馈信息的级别，共3个级别，-v -v -v将提供最详细的设置信息
-s: 用于指定伪随机数生成器的seed值，如果seed相同，则两次Monkey测试所产生的事件序列也相同的

五、关于Monkey测试的停止条件
Monkey Test执行过程中在下列三种情况下会自动停止：
1、如果限定了Monkey运行在一个或几个特定的包上，那么它会监测试图转到其它包的操作，并对其进行阻止。
2、如果应用程序崩溃或接收到任何失控异常，Monkey将停止并报错。
3、如果应用程序产生了应用程序不响应(application not responding)的错误，Monkey将会停止并报错。
通过多次并且不同设定下的Monkey测试才算它是一个稳定性足够的程序。

六、Monkey选项在实际测试中的运用
adb shell monkey 
    -p com.amaker.mp 
    -s 300 
    --throttle 300 
    --ignore-crashes 
    --ignore-timeouts 
    --monitor-native-crashes 
    -v -v 1000 > C:\java_monkey_log.txt
七、结果分析
一般的测试结果分析：
1.ANR问题：在日志中搜索“ANR”
2.崩溃问题：在日志中搜索“Exception”, “Crash”, “error”

第一步：adb  shell ps | grep【findstr】 monkey 查找到正在测试的monkey包名
第二步：kill  pid：删除查找出的monkey进程
以上完美的停止monkey测试

--ADB 常用命令
adb devices --查看当前连接设备
adb reboot  --重启系统（重启手机）
adb kill-server --杀死进程adb
adb start-server --重启ADB服务
adb install xxx.apk --安装某APK文件
adb install -r xxx.apk --覆盖安装
adb install -r -t xxx.apk  --run出来的包，只是test-only属性的时候
adb uninstall 包名xxx  --卸载
adb uninstall -k com.zhy.app --卸载apk但保留数据
adb push 文件名 手机端SDCard路径 --电脑端上传数据到手机端（上传文件）
adb pull /sdcard/xxx.txt  --手机端下载数据到电脑端（下载文件）
举例子：
adb -s devicel install xxx.apk

adb logcat --查看日志

--ADB Shell 命令
adb shell dumpsys activity | findstr "mFocusedActivity" (window cmd命令) --查看当前页面
adb shell dumpsys activity | findstr -i run --查看当前运行的页面[windows]
adb shell dumpsys activity | grep "mFocusedActivity"  (linux + mac) --查看当前页面
adb shell dumpsys activity | grep -i run  --查看当前运行的页面[linux]

adb shell pm list packages -- 查看所有的包名
adb shell am start 包名/完整Activity路径 --启动某个APP的启动页
adb shell am start -a "android.intent.action,VIEW" -d "https://www.google.com" --启动一个隐式的Intent
adb shell am broadcast -a "broadcastactionfilter" -- 发送广播
adb shell am broadcast -a "broadcastactionfilter" -e name zhy --如果需要携带参数（携带一个Intent,key为name）
adb shell am startservice "com.zhy.aaa/com.zhy.aaa.MyService" --启动一个服务
adb shell screencap /sdcard/screen.png --截图
adb shell screenrecord /sdcard/demo.mp4 --录制视频 注：此命令适用于Android 4.4及以上的设备中。 
录制视频也有参数选项，比如 --size 设置视频大小， --time-limit设置最大录制时长等。

--input:事件输入
adb shell input text "insert%stext%shere" --使用adb shell input命令向屏幕输入一些信息，注意：%s表示空格。
adb shell input tap 500 1450 --模拟屏幕点击事件
adb shell input swipe 100 500 100 1450 100 --模拟手势滑动事件：表示从屏幕坐标（100,500）开始，滑动到(100,1450)结束，整个过程耗时100ms.
adb shell input swipe 100 500 100 500 500 --模拟长按 ： 同一个坐标 耗时长些
adb shell input keyevent 25 --模拟点按实体按钮的命令

--am(Activity Manager)命令来启动一个APP、启动Activity、启动广播和服务等等。
adb shell am start com.example.crime/com.example.crime.MainActivity
adb shell am force-stop app包名 --关闭包
adb shell pm clear app com.android.settings --关闭包
adb shell am start com.example.crime/com.example.crime.SecondActivity -e argus_name QiuShui -- -e argus_name传参
adb shell am start -a "android.intent.action.VIEW" -d "https://www.google.com"
adb shell am broadcast -a "our.specified.action"
adb shell am broadcast -a android.intent.action.BOOT_COMPILETED --手机重启
adb shell am startservice "com.example.crime/com.example.crime.MyService" --启动某服务

启动带的参数一般是Key-value形式，这里的key是argus_name,Value是QiuShui.
除了默认启动的activity外，打开其他的activity时，需要在清单文件中添加android:exported="true"属性。
要启动一个隐式的Intent，也就是说需要传入action等参数，在ADB调试桥中可以得知Intent的参数规范，
比如-a表示action,-c表示category,-d表示data_uri,-e表示添加额外Key-Value信息。例如：

--事件输出
adb logcat
adb shell service list
服务	            类名	                    功能
activity	ActivityManagerService	AMS相关信息
package	    PackageManagerService	PMS相关信息
window	    WindowManagerService	WMS相关信息
input	    InputManagerService	    IMS相关信息
power	    PowerManagerService 	PMS相关信息
procstats	ProcessStatsService	    进程统计
battery	    BatteryService	        电池信息
alarm	    AlarmManagerService	    闹钟信息
meminfo	    MemBinder	            内存
例如，要查看电池信息，命令行输入adb shell dumpsys battery，可以看到如下图:

adb shell dumpsys activity
adb shell dumpsys activity | grep -i 'run'
adb shell dumpsys activity | findstr -i 'run'

--adb shell dumpsys window 
  -- 
  window displays --分辨率
  adb shell dumpsys window policy | findstr isStatusBarKeyguard --查看手机锁屏状态

    adb shell dumpsys window policy | findstr isStatusBarKeyguard   （守卫者状态：电源键）
    adb shell dumpsys window policy | findstr mShowingLockscreen  （显示锁定屏幕）
  window policy 
  window token
  window animator
  window windows
  window displays
adb shell dumpsys activity intents

--查看进程信息
adb shell ps  --查看进程
adb shell top --系统CPU

--获取手机系统等一些基本信息，手机硬软件等信息
adb shell "cat /system/build.prop | grep "product"" --获取手机系统信息（ CPU，厂商名称等）
adb shell getprop ro.build.version.release --获取手机系统版本
adb shell getprop ro.build.version.sdk --获取手机系统api版本
adb -d shell getprop ro.product.model --获取手机设备型号
adb -d shell getprop ro.product.brand --获取手机厂商名称
adb get-serialno --获取手机的序列号1
adb shell getprop ro.serialno --获取手机的序列号2
adb shell dumpsys iphonesubinfo --获取手机的IMEI-1
adb shell getprop gsm.baseband.imei --获取手机的IMEI-2
service call iphonesubinfo 1  --获取手机的IMEI-3
adb shell cat /proc/meminfo --获取手机内存信息
adb shell dumpsys window displays --获取手机分辨率
adb shell wm density --获取手机物理密度

Appium API 使用大全
-- 强制等待：time.sleep()
-- 隐式等待: driver.implicitly_wait(20) --appium 隐式等待(用来等待页面加载完成)有点保障所有元素加载好，缺点：耗时太长
-- 显示等待: 方法:WebDriverWait(driver, timeout, poll_frequency).until(method) --在一个超时时间范围内，每隔一段时间去搜索一次元素是否存在
// 在Appium中用了Selenium中造的轮子(显示等待)
方法:WebDriverWait(driver, timeout, poll_frequency).until(method)
    参数：
        1.driver：手机驱动对象
        2.timeout：搜索超时时间
        3.poll_frequency：每次搜索间隔时间，默认时间为0.5s
        4.method：定位方法(匿名函数)
匿名函数:
    lambda x: x
等价于python函数：
    def test(x):
        return x

使用示例：
        from selenium.webdriver.support.wait import WebDriverWait
        WebDriverWait(driver, timeout, poll_frequency).until(lambda x: x.find_elements_by_id(id_value))
    解释：
        1.x传入值为：driver，所以才可以使用定位方法.
    函数运行过程：
        1.实例化WebDriverWait类，传入driver对象，之后driver对象被赋值给WebDriverWait的一个类变量：self._driver
        2.until为WebDriverWait类的方法，until传入method方法(即匿名函数)，之后method方法会被传入self._driver
        3.搜索到元素后until返回定位对象，没有搜索到函数until返回超时异常错误.
业务场景:
        1.进入设置页面
        2.通过ID定位方式点击搜索按钮 
代码实现：# 导入WebDriverWait类，用了selenium中的显示等待的轮子
    from selenium.webdriver.support.wait import WebDriverWait
    # 超时时间为30s，每隔1秒搜索一次元素是否存在，如果元素存在返回定位对象并退出
    search_button = WebDriverWait(driver, 30, 1).until(lambda x: x.find_elements_by_id(com.android.settings:id/search))
    search_button.click()
    driver.quit()
--Appium-- 应用操作
--java
driver.installApp("path/to/my.apk") --apk在项目绝对路径
driver.installApp("D:\\android\\apk\\my.apk")  --apk在电脑硬件中
driver.removeApp("包名") --从设备中删除一个应用
driver.closeApp() --关闭打开的应用，当前打卡的应用。== 按Home键应用置于后台
driver.launchApp() --启动应用 配合closeApp() 使用
driver.isAppInstalled("包名") --检查应用是否已经安装，传包名。
driver.runAppInBackground(time) --将当前的活跃的应用程序发送到后台。需要入参时长
driver.reseetApp() --重置当前被测程序到初始化状态。该方法不需要入参
--python
driver.installApp("path/to/my.apk") --apk在项目绝对路径
driver.installApp("D:\\android\\apk\\my.apk")  --apk在电脑硬件中
driver.removeApp("包名") --从设备中删除一个应用
driver.close_app() --关闭打开的应用，当前打卡的应用。== 按Home键应用置于后台
driver.launch_app() --启动应用 配合closeApp() 使用
driver.isAppInstalled("包名") --检查应用是否已经安装，传包名。
driver.background_app(seconds) --将当前的活跃的应用程序发送到后台。需要入参时长
driver.reset()
--Fiddler 连接安卓手机-----
1.打开Fiddler 下载证书到桌面，将证书安装到安卓机上：安卓机操作：设置-搜索安装网络证书-从设备存储安装安全证书
fiddler打开的断口为：8866
2.fiddler打开设置页，打开运行远程https 运行连接。
3.电脑本机：10.49.107.108 

--Appium-- TouchAction


--selenium  --问题罗列 

1 -- selenium.common.exceptions.WebDriverException: 
        Message: An unknown server-side error occurred while processing the command.
原因：

--促销中心问题-数据库迁移
1 oracle迁移到MySQL 
pmc_task :接口 迁移到MySQL落库了。
非pmc_task:接口 数据库未迁移到MySQL，依旧还是在oracle。导致非pmc_task接口，查询或者生失效接口，找不到活动编号。

解决方案：将pmc_task落库到oracle，回退到之前的状态。


======实战------ 全民小视频=登录用户名+密码
13122395209
Aa1234123456789

遇到问题
1. 使用appium在android7.0真机上测试程序时报错command failed shell "ps 'uiautomator'"的解决方式
第一步：由于真机测试 会自动安装，两个软件：要使用ADB命令先将已安装的APK卸载掉：
   这两：package:io.appium.settings,package:io.appium.unlock
   代码：quanmin_xiaoshipin==>adb_common()方法中。请查看 
第二步： 修改Appium里面的代码
   参考博主：https://blog.csdn.net/pjl6523853/article/details/72886048
   
2.