from machine import *
from config import *
from time import sleep
try:
    from microbit import Image, display
except ImportError:
    class Image:
        YES = NO = ARROW_W = ARROW_E = HAPPY = None
    class Display:
        def show(self, icon): print(f"显示图标: {icon}")
    display = Display()

def vibrate(duration_ms = 100, intensity = 175):
    """控制震动电机"""
    VIBRATION_MOTOR.write_analog(intensity)
    sleep(duration_ms)
    VIBRATION_MOTOR.write_analog(0)
    
def play_sound(freq = 440, duration = 100):
    """蜂鸣器发声"""
    BUZZER.write_analog(512)  # 50% 占空比
    BUZZER.set_analog_period_microseconds(int(1000000/freq))
    sleep(duration)
    BUZZER.write_analog(0)
    
def show_icon(icon_name):
    """显示预设图标"""
    icons = {
        'ok': Image.YES,
        'no': Image.NO,
        'left': Image.ARROW_W,
        'right': Image.ARROW_E
    }
    display.show(icons.get(icon_name, Image.HAPPY))