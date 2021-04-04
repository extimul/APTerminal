import random
import time


class Ruder:
    def __init__(self):
        print('Ruder is init')

    @staticmethod
    def get_data(move):
        # time.sleep(0.1)
        a = random.randint(0, 5000)
        return str(move)


class XSense:
    def __init__(self):
        print('XSense is init')

    @staticmethod
    def get_data():
        time.sleep(0.003)
        return '-0.20695334794058803;-0.200084414093397;9.865049590444537;0.0011026859284082563;' \
                '-0.014553965594061037;0.002864003181622525;0.0;0.0;0.0;'


class RTK:
    def __init__(self):
        print('RTK is init')

    @staticmethod
    def get_data():
        time.sleep(1)
        return '187065.69;383136.022;1;EHT+108.966;'
