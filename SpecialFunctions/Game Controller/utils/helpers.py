from machine import *
from time import sleep

def debounce(pin, delay = 20):
    """按钮去抖动"""
    initial = pin.read_digital()
    sleep(delay)
    return pin.read_digital() if pin.read_digital() == initial else initial

def map_value(value, in_min, in_max, out_min, out_max):
    """数值映射"""
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def clamp(value, min_val, max_val):
    """限制范围"""
    return max(min_val, min(max_val, value))