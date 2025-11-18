from microbit import *
from config import *
import radio

class Wireless:
    def __init__(self):
        radio.on()
        radio.config(group=RADIO_GROUP)
        
    def send_command(self, cmd_type, value = None):
        """发送标准化命令"""
        if cmd_type == 'joystick':
            x, y, btn = value
            radio.send(f"J,{x},{y},{int(btn)}")
        elif cmd_type == 'button':
            radio.send(f"B,{value[0]},{int(value[1])}")

    def receive(self):
        """接收并解析命令"""
        msg = radio.receive()
        if msg:
            parts = msg.split(',')
            if parts[0] == 'J':
                return ('joystick', (int(parts[1]), int(parts[2]), bool(parts[3])))
            elif parts[0] == 'B':
                return ('button', (parts[1], bool(parts[2])))
        return None