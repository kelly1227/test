包名

com.shanghaigm.mychevy/com.uaes.vkmdemoapp.MainActivity
adb install 路径（电脑里）
adb uninstall com.shanghaigm.mychevy
adb shell am start -n com.shanghaigm.mychevy/com.uaes.vkmdemoapp.MainActivity

LSGKM8S23KW003084  13122395209
LSGKM8S24KW999980
LSGKJ8RH8KW000183  13122395209

adb shell monkey -p com.shanghaigm.mychevy -s 500 --throttle 300 --ignore-crashes --ignore-timeouts --monitor-native-crashes -v -v 1000 > D:\java_monkey_log.txt