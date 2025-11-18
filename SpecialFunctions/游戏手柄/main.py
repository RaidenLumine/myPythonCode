from microbit import *
from config import *
from modules.joystick import *
from modules.buttons import ButtonHandler
from modules.feedback import *
from modules.communication import Wireless

def main():
    # 初始化
    wireless = Wireless()
    btn_handler = ButtonHandler()
    display.show(Image.HAPPY)
    
    while True:
        # 读取输入
        joy_x, joy_y, joy_btn = read_joystick()
        btn_changes = btn_handler.check_buttons()
        
        # 发送控制命令
        wireless.send_command('joystick', (joy_x, joy_y, joy_btn))
        for btn, state in btn_changes.items():
            wireless.send_command('button', (btn, state))
            if state: vibrate(50) # 按钮按下反馈
            
        # 接收处理
        cmd = wireless.receive()
        if cmd:
            if cmd[0] == 'button' and cmd[1][1]:
                play_sound(523)
                
        sleep(20) # 控制循环频率

if __name__ == "__main__":
    main()