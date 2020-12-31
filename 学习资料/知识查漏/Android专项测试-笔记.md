# Android篇

## 1. 性能测试

- Android性能测试分为两类：
  1、一类为rom版本（系统）的性能测试
  2、一类为应用app的性能测试
- Android的app性能测试包括的测试项比如：
  1、资源消耗
  2、内存泄露
  3、电量功耗
  4、耗时
  5、网络流量消耗
  6、移动终端相关资源利用率
  7、帧率
  8、渲染等等....
- 表格
- 
- 工具：
  （工具的原理都是基于调用android底层的一些api来获取到测试所用到的值）GT等
- 测试方法：
  1、设计场景 ：手工或自动化场景
  2、获取数据：可获取的数据包括：内存、cpu、电量功耗、hprof（内存泄露分析文件）、响应时间等等。。。。配合手工或自动化场景来获取数据（最好多取几次而且每次配合不同的设备看平均值）作为最后的对比分析
  3、结果分析 ：拿到数据后分析哪些模块的数据异常再去Check code定位问题的原因
- Android系统的几种场景状态：
  1、空闲状态： 指打开应用后，点击home键让应用后台运行，此时应用处于的状态叫做空闲
  2、中等规格和满规格状态：中等规格和满规格指的是对应用的操作时间的间隔长短不一，中等规格时间较长，满规格时间较短

### 1.1 内存篇

> **背景知识：**
> C/C++申请的内存空间在native heap中，而java申请的内存空间则在dalvik heap中。这个是因为Android系统对dalvik的vmheapsize作了硬性限制，当java进程申请的java空间超过阈值时，就会抛出OOM异常（这个阈值可以是48M、24M、16M等，视机型而定），可以通过adb shell getprop | grep dalvik.vm.heapgrowthlimit查看此值。也就是说，程序发生OMM并不表示RAM不足，而是因为程序申请的java heap对象超过了dalvik vmheapgrowthlimit。也就是说，在RAM充足的情况下，也可能发生OOM。
>
> 这样的设计似乎有些不合理，但是Google为什么这样做呢？这样设计的目的是为了让Android系统能同时让比较多的进程常驻内存，这样程序启动时就不用每次都重新加载到内存，能够给用户更快的响应。迫使每个应用程序使用较小的内存，移动设备非常有限的RAM就能使比较多的app常驻其中。但是有一些大型应用程序是无法忍受vmheapgrowthlimit的限制的
>
> 实际上dalvik.vm.heapgrowthlimit和dalvik.vm.heapsize都是java虚拟机的最大内存限制，应用如果不想在dalvikheap达到heapgrowthlimit限制的时候出现OOM，需要在Manifest中的application标签中声明android：largeHeap=“true”，声明后应用dalvik heap达到heapsize的时候才会出现OOM

1. 内存测试中的测试子项：
   1）空闲状态下的应用内存消耗情况
   2）中等规格状态下的应用内存消耗情况
   3）满规格状态下的应用内存消耗情况
   4）应用内存峰值情况
   5）应用内存泄露情况
   6）应用是否常驻内存
   7）压力测试后的内存使用情况
2. 内存问题现象：
   1）内存抖动
   2）大内存对象被分配
   3）内存不断增长
   4）频繁GC
3. 内存数据获取：
   1、各种linux命令（top、free、meminfo…）
   2、通过dumpsys
   `adb shell dumpsys meminfo [pakagename | pid]`
   3、通过/system/xbin/procrank工具
   `adb shell procrank`
   说明：
   VSS – Virtual Set Size 虚拟耗用内存（包含共享库占用的内存）
   RSS – Resident Set Size 实际使用物理内存（包含共享库占用的内存）
   PSS – Proportional Set Size 实际使用的物理内存（比例分配共享库占用的内存）
   USS – Unique Set Size 进程独自占用的物理内存（不包含共享库占用的内存） USS 是针对某个进程开始有可疑内存泄露的情况，是一个程序启动了会产生的虚拟内存，一旦这个程序进程杀掉就会释放。不过USS需要通过root的手机。一般没有root的手机我们可以获取PSS。而PSS通过如下命令来获取：`adb shell dumpsys meminfo <Package Name>|grep TOTAL`
   4、通过android提供的procrank
   1）首先去google获取procrank、procmem、libpagemap.so三个文件
   2）然后push文件，执行 adb push procrank /system/xbin adb push procmem
   /system/xbin adb push libpagemap.so /system/lib
   3）赋权 adb shell chmod 6755 /system/xbin/procrank adb shell chmod 6755 /system/xbin/procmem adb shell chmod 6755 /system/lib/libpagemap.so ,
   4）在开启工具记录 adb shell procrank |grep packagename >/address/procrank.txt
   5、通过android提供的ActivityManager的getMemoryInfo(ActivityManager.MemoryInfo outInfo)（这个方法是写一个简单的app去监控的时候用到的，轻便简单）

```
private void GetMemory() {    final ActivityManager activityManager = (ActivityManager) getSystemService(ACTIVITY_SERVICE);        ActivityManager.MemoryInfo info = new ActivityManager.MemoryInfo();       activityManager.getMemoryInfo(info);        Log.i(tag,"系统剩余内存:"+(info.availMem >> 10)+"k");       Log.i(tag,"系统是否处于低内存运行："+info.lowMemory);    Log.i(tag,"当系统剩余内存低于"+info.threshold+"时就看成低内存运行");}
6、Memory  Monitor （android studio的插件）  【makedown？？？】

4. /proc/meminfo文件里列出的字段解释：
```

> MemTotal: 所有可用RAM大小。 MemFree: LowFree与HighFree的总和，被系统留着未使用的内存。
> Buffers: 用来给文件做缓冲大小。 Cached: 被高速缓冲存储器（cache memory）用的内存的大小（等于diskcache
> minus SwapCache）。 SwapCached:被高速缓冲存储器（cache
> memory）用的交换空间的大小。已经被交换出来的内存，仍然被存放在swapfile中，用来在需要的时候很快的被替换而不需要再次打开I/O端口。
> Active: 在活跃使用中的缓冲或高速缓冲存储器页面文件的大小，除非非常必要，否则不会被移作他用。 Inactive:
> 在不经常使用中的缓冲或高速缓冲存储器页面文件的大小，可能被用于其他途径。 SwapTotal: 交换空间的总大小。 SwapFree:
> 未被使用交换空间的大小。 Dirty: 等待被写回到磁盘的内存大小。 Writeback: 正在被写回到磁盘的内存大小。
> AnonPages：未映射页的内存大小。 Mapped: 设备和文件等映射的大小。 Slab:
> 内核数据结构缓存的大小，可以减少申请和释放内存带来的消耗。 SReclaimable:可收回Slab的大小。
> SUnreclaim：不可收回Slab的大小（SUnreclaim+SReclaimable＝Slab）。
> PageTables：管理内存分页页面的索引表的大小。 NFS_Unstable:不稳定页表的大小。

```
5. android检查内存泄露步骤：
```

1、运行Monkey进行压力测试：
`adb shell monkey -p cn.microinvestment.weitou --pct-touch 100 --ingore-crashes --throttle 1000 -s 100 -v -v 50`
2、监控内存值，如果出现过大等递增异常则保存HPROF文件（hprof文件是Java 虚拟机的Heap快照）用于分析查看应用内存的命令：
`adb shell dumpsys meminfo cn.microinvestment.weitou(进程名)`
如果发现内存过大，则保存HPROF文件：`adb shell am dumpheap <进程名> <保存路径>`
3、分析hprof文件
用工具MAT来查看，首先还要这个HPROF文件转换成MAT可读的文件
在Android SDK tool里面有个hprof-conv命令：
hprof-conv <原HPROF文件路径> <转换后的HPROF路径>
`hprof-conv a.hprof b.hprof`
4、用MAT工具打开转换后的HPROF文件
一般选择Leak Suspects Report（通过SQL语句来查询对象有没有被释放掉，如果有多个相同的对象，则会存在内存泄露的问题）

### 1.2 CPU篇

1. CPU测试中的测试子项：
   1）空闲状态下的应用CPU消耗情况
   2）中等规格状态下的应用CPU消耗情况
   3）满规格状态下的应用CPU消耗情况
   4）应用CPU峰值情况
2. CPU数据获取：
   1）`adb shell dumpsys cpuinfo | grep packagename`
   2)top命令
   `adb shell top -m 10 -s cpu` #查看占用cpu最高的前10个程序（-t 显示进程名称，-s 按指定行排序，-n 在退出前刷新几次，-d 刷新间隔，-m 显示最大数量）
   `adb shell top | grep PackageName > /address/cpu.txt`

### 1.3 流量篇

1. 概念：
   中等负荷：应用正常操作
   高负荷：应用极限操作
2. 流量测试中的测试子项：
   1、应用首次启动流量值
   2、应用后台连续运行 2 小时的流量值
   3、应用高负荷运行的流量峰值
   4、应用中等负荷运行时的流量均值
3. 获取流量数据：
   1、tcpdump＋wireshark
   2、/proc/net/目录下相关文件
   cat /proc/net/dev 获取系统的流量信息
   3、查询应用的pid： adb shell ps | grep tataufo #如：31002
   通过PID获取该应用的流量数据： adb shell cat /proc/31002/net/dev
   （wlan0代表wifi上传下载量标识, 单位是字节可以/1024换算成KB, 打开手机飞行模式再关掉就可以将wlan0中的值初始化0）
   4、查询应用的pid： adb shell ps | grep tataufo #如：31002
   通过PID获取UID：adb shell cat /proc//status
   通过UID获取：adb shell cat /proc/net/xt_qtaguid/stats | grep 31002
   5、通过adb shell dumpsys package来获取应用的uid信息，然后在未操作应用之前，通过查看 ：
   adb shell cat /proc/uid_stat/uid/tcp_rcv
   adb shell cat /proc/uid_stat/uid/tcp_snd
   获取到应用的起始的接收及发送的流量，然后我们再操作应用，再次通过上述2条命令可以获取到应用的结束的接收及发送的流量，通过相减及得到应用的整体流量消耗
   6、Android代码：Android的TrafficStats类

### 1.4 功耗篇

1. 功耗测试中的测试子项：
   1、手机安装目标APK前后待机功耗无明显差异
   2、常见使用场景中能够正常进入待机，待机电流在正常范围内
   3、长时间连续使用应用无异常耗电现象
2. 功耗测试方法：
   方法一：软件
   1、采用市场上提供的第三方工具，如金山电池管家之类的。
   2、就是自写工具进行，这里一般会使用3种方法：
   1）基于android提供的PowerManager.WakeLock来进行
   2）比较复杂一点，功耗的计算=CPU消耗+Wake lock消耗+数据传输消耗+GPS消耗+Wi-Fi连接消耗
   3）通过 adb shell dumpsys battery来获取
   3、battery-historian（google开源工具）
   方法二：硬件
   一般使用万用表或者功耗仪安捷伦进行测试，使用功耗仪测试的时候，需要制作假电池来进行的，有些不能拔插电池的手机还需要焊接才能进行功耗测试

### 1.5 GPU篇（FPS）

1. 概念：
   **过度绘制：** 界面显示的activity套接了多层而导致
   **帧率：**屏幕滑动帧速率
   **帧方差：** 屏幕滑动平滑度
   **FPS：**Frames Per Second 每秒显示的帧数 根据人眼的生理结构，帧率高于24时就被认为是连贯的。对于游戏画面30fps是最低能接受的，60fps逼真感，如果帧率高于屏幕刷新频率就是浪费。要达到30fps，每帧所占用的时间要小于33毫秒
2. GPU测试中的测试子项：
   1、界面过度绘制
   2、屏幕滑动帧速率
   3、屏幕滑动平滑度
3. 过度绘制测试：（人工进行测试）
   打开开发者选项中的显示GPU过度绘制（Debug GPU overdraw）
   验收的标准:
   1、不允许出现黑色像素
   2、不允许存在4x过度绘制
   3、不允许存在面积超过屏幕1/4区域的3x过度绘制（淡红色区域）
4. 屏幕滑动帧速率测试：
   方法一：
   1.手机端打开开发者选项中的启用跟踪后勾选Graphics和View
   2.启动SDK工具Systrace，勾选被测应用，点击Systrace，在弹出的对话框中设置持续抓取时间，在trace taps下面勾选gfx及view选项
   3.手工滑动界面可以通过节拍来进行滑动或者扫动，帧率数据会保存到默认路径下，默认名称为trace.html
   4.将trace.html文件拷贝到linux系统下通过命令进行转换，生成trace.csv文件
   grep 'postFramebuffer' trace.html | sed -e 's/.*]\W*//g' -e 's/:.*$//g' -e 's/.//g' > trace.csv
   5.用excel打开文件计算得到帧率
   方法二：
   硬件的方法，打开高速相机，开启摄像模式，录制手工滑动或者扫动被测应用的视频，再通过人工或者程序数帧的方法对结果进行计算得到帧率
5. 屏幕滑动平滑度的测试：
   方法如同帧率测试，唯一的差异就是最后的结果计算公式的差异
6. 捕获app帧率（android流畅度FPS测试）：
   1、打开手机开发者选项，勾选GPU显示配置文件（系统会记录保留每个界面最后128帧图像绘制的相关时间信息）
   2、adb shell dumpsys gfxinfo com.xxx.xxx > zinfo.txt
   3、结果数据分析
   Profile data in ms部分：
   Draw： 创建显示列表的时间（DisplayList），所有View对象OnDraw方法占用的时间
   Process： Android 2D渲染引擎执行显示列表所花的时间，View越多时间越长
   Execute：将一帧图像交给合成器（compsitor）的时间，较小
7. 其他工具：
   GameBench 测试android app的FPS工具
   Gfxinfo 查看app绘制性能工具

### 1.6 响应时间篇

1. 理解：
   1）从单击事件触发到容器启动NativeAPP消耗的时间（埋点）
   2）NativeAPP完整启动消耗的时间（可以通过system.log获取）
   3）Native调用RPC请求方法的延迟时间（埋点）
   4）RPC请求发出去过程中的具体数据（req_size req_header req_time等，通过埋点获取）
   5）RPC请求返回的具体数据（res_size res_header res_time等，通过埋点获取）
   6）本地解析返回数据所消耗的时间（埋点或者TraceView工具可获取）
   7）界面渲染的时间（可以通过慢速摄像机或者埋点获取）
2. android app启动时间测试
   （安卓Activity启动过程性能剖视: http://www.rudy-yuan.net/archives/59/）
3. 应用的启动时间的测试，分为三类：
   1）首次启动 --应用首次启动所花费的时间
   2）非首次启动 --应用非首次启动所花费的时间
   3）应用界面切换--应用界面内切换所花费的时间
4. 应用启动时间数据获取：
   1、`adb logcat > /address/logcat.txt` #所有activity打印的日志
   `find “Displayed” /address/logcat.txt > /newaddress/fl.txt` #通过日志过滤关键字Displayed来过滤
   `find “ActivityName” /newaddress/fl.txt > /newaddress/last.txt` #通过activity名来过滤获取所测应用
   通过计算activity最后剩余的时间之和即可
   2、硬件测试， 使用高速相机或者手机采用录像的方法把应用启动过程给录制下来，然后通过人工数帧或者程序数帧的方式计算启动时间

## 2 弱网测试

1. 测试方法：
   1、使用真实的SIM卡、运营商网络来进行测试（移动无线测试中存在一些特别的BUG必须在特定的真实的运营商网络下才会发现）
   2、通过代理的方式模拟弱网环境进行测试（charles 硬延迟）
   3、连接模拟弱网的热点进行测试
2. 热点模拟方法：
   1）通过设置iPhone的开发者模式之后共享热点（硬延迟）
   2）FaceBook开源的ATC（可使用树莓派来搭建ACT环境）
3. 用户体验需要做的：
   1）在应用中统一弱网加载的界面样式、动画效果、菊花icon等
   2）统一网络错误、服务端错误、超时等展现给用户的界面和提示语句
   3）定义清楚在每个中间过程是的用户交互行为

转自：https://www.zybuluo.com/defias/note/592309