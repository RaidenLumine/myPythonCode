from microbit import *
from config import *

def read_joystick():
    """读取摇杆状态并返回标准化坐标(-100~100)"""
    x_raw = JOYSTICK_X_PIN.read_analog()
    y_raw = JOYSTICK_Y_PIN.read_analog()
    
    # 应用死区
    if abs(x_raw) < DEAD_ZONE: x_raw = 0
    if abs(y_raw) < DEAD_ZONE: y_raw = 0

    # 标准化到 -100~100
    x = int(x_raw * 100 / 511)
    y = int(y_raw * 100 / 511)
    btn_pressed = JOYSTICK_BTN_PIN.read_digital() == 0

    return x, y, btn_pressed

def get_direction():
    """返回方向字符串描述"""
    x,y,_ = read_joystick()
    if y<-50: return "UP"
    if y>50: return "DOWN"
    if x<-50: return "LEFT"
    if x>50: return "RIGHT"
    return "CENTER"