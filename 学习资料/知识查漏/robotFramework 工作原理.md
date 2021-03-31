Robotframework 简介及工作原理
　　下面通过官网和网上资料来简单介绍下Robotframework及其工作原理。

　　官方说明：

　　Robot Framework is a generic test automation framework for acceptance testing and acceptance test-driven development (ATDD). It has easy-to-use tabular test data syntax and it utilizes the keyword-driven testing approach. Its testing capabilities can be extended by test libraries implemented either with Python or Java, and users can create new higher-level keywords from existing ones using the same syntax that is used for creating test cases.

　　翻译如下：

　　Robot Framework是用于验收测试和验收测试驱动开发（ATDD）的通用测试自动化框架。 它具有易于使用的表格测试数据语法，并使用关键字驱动的测试方法。 它的测试功能可以通过使用Python或Java实现的测试库进行扩展，用户可以使用与创建测试用例相同的语法，从现有的关键字创建新的更高级别的关键字。

　　我的理解如下：

　　Robot Framework是一个完全基于关键字测试驱动的框架，它即能够基于它的一定规则，导入你需要的测试库（例如：其集成了selenium的测试库，即可以理解为操作web控件的测试底层库），然后基于这些测试库，你能应用HTML、TXT等文档形式编写自己的关键字（这些关键字即你的库组成），之后，再编写测试用例（测试用例由测试关键字组成）进行测试。例如：一个简单的登陆测试由：登陆+输入密码+登出三个关键字组成，也可以由一个关键字登陆组成，关键字颗粒的大小可以自行定制。

　　主要包括：

　　内置标准库，如BuiltIn

　　外部（第三方）扩展库，如Selenium2Library

　　关键字，主要包括总是可用的内置关键字，来自导入测试库的库关键字和用户在创建测试用例时使用表格语法创建的用户关键字

　　创建测试，主要包括测试项目、套件、用例

　　运行测试

　　生成测试报告，会生成三个文件：Output.xml、Log.html、Reprot.html，其中Log.html主要用于展示测试脚本的执行过程，report.html为测试报告，展示测试用例的运行情况及结果。

　　工作原理：

　　Robot Framework的基本运行流程如下：

　　1、Robot开始测试是从cmd输入命令，初始运行程序接收命令字符（主要是用txt或html写的测试用例集）

　　2、接收之后，robot先生成初始化全局变量配置，主要是定义一系列的字段名称和文件名称（例如：日志文件名称等）（由settings.py中的类完成）

　　3、然后，开始解析用例文件，生成数据对象，数据对象中包含了测试集的各种数据，例如：测试用例集名称、各个测试用例名称、各个关键字名称等

　　4、再将测试数据对象传送给测试集合类处理，生成测试集suite对象

　　5、紧接着运行suite中的用例测试，然后调用关键字，找到关键字对应的库文件，进行操作

　　6、将每一个操作和结果都写在输出的xml文件中（有专门调用对输出xml进行操作的类）

　　7、最后待测试完成后，调用转换类将xml文件转换成相应的HTML日志报告，测试完成。

　　

　　从Robot Framework的工作原理上，我们可以很好的学习到关键字测试驱动思想和数据测试驱动思想的应用。

 
