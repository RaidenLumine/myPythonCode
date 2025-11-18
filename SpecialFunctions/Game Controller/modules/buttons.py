from machine import *
from config import *
from utils.helpers import debounce

class ButtonHandler:
    def __init__(self):
        self.last_state = {
            'A': False,
            'B': False,
            'X': False,
            'Y': False
        }
        
    def check_buttons(self):
        """返回所有按钮状态变化的字典"""
        current = {
            'A': debounce(BUTTON_A_PIN),
            'B': debounce(BUTTON_B_PIN),
            'X': debounce(BUTTON_X),
            'Y': debounce(BUTTON_Y)
        }
        
        changes = {}
        for btn in current:
            if current[btn] != self.last_state[btn]:
                changes[btn] = current[btn]
                
        self.last_state = current
        return changes