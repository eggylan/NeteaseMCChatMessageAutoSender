import pyautogui
import time
import keyboard

def stop_loop():
    global running
    running = False

print("欢迎使用Minecraft基岩版聊天消息自动发送器！\n本脚本通过模拟按键实现自动发送。")
choose = int(input("请选择你要使用的模式，输入1为“↑键+回车”模式，输入2为“复制粘贴”模式："))

if choose == 1:
    print("请先将要发送的信息置于聊天框内，然后启动本脚本")
    print("若想提前结束发送，请在脚本开始运行后按键盘上的U键")
    a = int(input("请输入你要发送消息的条数（必须为整数）："))
    b = float(input("请输入消息发送的时间间隔（单位：秒）："))
    print("==7秒钟后自动执行==")
    time.sleep(7)
    print("==开始执行==")

    keyboard.add_hotkey('u', stop_loop)

    running = True
    for _ in range(a):
        if not running:
            break
        pyautogui.press('enter')
        pyautogui.press('up')
        time.sleep(b)
    
    keyboard.remove_hotkey('u')
    print("==脚本运行结束==")
    input("按回车键退出...")

elif choose == 2:
    print("请先复制要发送的文本，然后启动本脚本")
    print("若想提前结束发送，请在脚本开始运行后按键盘上的U键")
    a = int(input("请输入你要发送消息的条数（必须为整数）："))
    b = float(input("请输入消息发送的时间间隔（单位：秒）："))
    print("==7秒钟后自动执行==")
    time.sleep(7)
    print("==开始执行==")

    keyboard.add_hotkey('u', stop_loop)

    running = True
    for _ in range(a):
        if not running:
            break
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(b)

    keyboard.remove_hotkey('u')
    print("==脚本运行结束==")
    input("按回车键退出...")

else:
    print("无效的选择，请选择1或2。")
    input("按回车键退出...")