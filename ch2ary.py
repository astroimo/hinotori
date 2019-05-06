import numpy as np
import re


def get_switch_info(text):
    switch = {}
    words = ''
    keys =  [  '100=', '101=', '102=', '200=', '201=', '202=',
                '300=', '301=', '302=', '400=', '401=', '402=',
                '500=', '501=', '502']

    with open(text) as afile:
        lines = afile.readlines()
    for line in lines:
        words += line
    for i,key in enumerate(keys):
        m = re.search(key,words)
        if words[m.end()] == 'o':
            switch[m.group()[:-1]] = words[m.end():m.end()+4]
        if words[m.end()] == 'c':
            switch[m.group()[:-1]] = words[m.end():m.end()+5]
    print(switch)
    return switch 

def ch01(switch):
    signal_from = m4(switch)
    return signal_from
    
def ch02(switch):
    signal_from = m11(switch)
    return signal_from

def ch03(switch):
    signal_from = m8(switch)
    return signal_from

def ch04(switch):
    signal_from = m10(switch)
    return signal_from 

def ch05(switch):
    signal_from = m7(switch)
    return signal_from

def ch06(switch):
    signal_from = m15(switch)
    return signal_from 


def m1_m4(switch):
    flow = switch['100']
    if flow == 'open':
        signal_from = None
    if flow == 'close':
        signal_from = 'ARY03'
    return signal_from

def m1_m8(switch):
    flow = switch['100']
    if flow == 'open':
        signal_from = 'ARY03'
    if flow == 'close':
        signal_from = None
    return signal_from

def m2_m8(switch):
    flow = switch['101']
    if flow == 'open':
        signal_from = None
    if flow == 'close':
        signal_from = 'ARY15'
    return signal_from

def m2_m7(switch):
    flow = switch['101']
    if flow == 'open':
        signal_from = 'ARY15'
    if flow == 'close':
        signal_from = None
    return signal_from

def m3_m5(switch):
    flow = switch['102']
    if flow == 'open':
        signal_from = 'ARY05'
    if flow == 'close':
        signal_from = None
    return signal_from 

def m3_m15(switch):
    flow = switch['102']
    if flow == 'open':
        signal_from = None
    if flow == 'close':
        signal_from = 'ARY05'
    return signal_from


def m4(switch):
    flow = switch['400']
    if flow == 'open':
        signal_from = m12(switch)
    if flow == 'close':
        signal_from = m1_m4(switch)
    return signal_from

def m5_m12(switch):
    flow = switch['401']
    if flow  == 'open':
        signal_from = m3_m5(switch)
    if flow  == 'close':
        signal_from = None
    return signal_from
    

def m5_m11(switch):
    flow = switch['401']
    if flow == 'open':
        signal_from = None
    if flow == 'close':
        signal_from = m3_m5(switch)
    return signal_from 

def m6_m11(switch):
    flow = switch['402']
    if flow == 'open':
        signal_from = None
    if flow == 'close':
        signal_from = 'ARY12'
    return signal_from

def m6_m10(switch):
    flow = switch['402']
    if flow == 'open':
        signal_from = 'ARY12'
    if flow == 'close':
        signal_from  = None
    return signal_from

def m7(switch):
    flow = switch['200']
    if flow == 'open':
        signal_from = 'ARY11'
    if flow == 'close':
        m2_m7(switch)
    return signal_from 

def m8(switch):
    flow = switch['201']
    if flow == 'open':
        signal_from = m2_m8(switch)
    if flow == 'close':
        signal_from = m1_m8(switch)
    return signal_from
        

def m9_m12(switch):
    flow = switch['202']
    if flow == 'open':
        signal_from = 'ARY07'
    if flow == 'close': 
        signal_from = None
    return signal_from

def m9_m14(switch):
    flow = switch['202']
    if flow == 'open':
        signal_from = None
    if flow == 'close':
        signal_from = 'ARY07'
    return signal_from

def m10(switch):
    flow = switch['500']
    if flow == 'open':
        signal_from = m6_m10(switch)
    if flow == 'close':
        signal_from = m14(switch)
    return signal_from

def m11(switch):
    flow = switch['501']
    if flow == 'open':
        signal_from = m6_m11(switch)
    if flow == 'close':
        signal_from = m5_m11(switch)
    return signal_from

def m12(switch):
    flow = switch['502']
    if flow == 'open':
        signal_from = m9_m12(switch)
    if flow == 'close':
        signal_from = m5_m12(switch)
    return signal_from

#def m13(): NOT USED

def m14(switch):
    flow = switch['301']
    if flow == 'open':
        signal_from = 'ARY16'
    if flow == 'close':
        signal_from = m9_m14(switch)
    return signal_from 

def m15(switch):
    flow = switch['302']
    if flow == 'open':
        signal_from = m3_m15(switch)
    if flow == 'close':
        signal_from ='ARY10'
    return signal_from 

def main():
    # for confermation
    #switch = {'100':'open','101':'open','102':'open','200':'open','201':'close','202':'open',\
    #          '300':'open', '301':'open','302':'open','400':'close','401':'close','402':'open',\
    #          '500':'open', '501':'open','502':'open'}
    TEXT = 'dummy.txt'
    switch = get_switch_info(TEXT)
    CHS = ['ch01', 'ch02', 'ch03', 'ch04', 'ch05', 'ch06']
    for ch in CHS:
        signal_from = eval(ch+'(switch)')
        print(ch,': ',signal_from)

if __name__=='__main__':
    main()

