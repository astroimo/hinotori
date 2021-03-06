import numpy as np
import re

#############################################################################
##this is a script to get bit-distribution in text/numpy format from Octad ##
#############################################################################

## TODO use'Class' !!
##----getting_if_switch_box_info----##

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







##------kiritori------##

INPUT=['./octadv1.out','./octadv2.out']     # log-file from octad while executing Expect == raw data 
                                            # the order should be octadv1, octadv2.
TOTAL=356274688       # total number of bit
OUT='./bit_dist.txt'  # output filename, please use '.npy' or '.txt'
ARRAY_NUM=16           # number of total possible array
LEVEL_NUM=8           # number of using level

#output format(default) **Rewrite 'def format()' when changing the format.
FORMAT=['#       A01        A02        A03        A04        A05        A06        A07        A08        A09        A10        A11        A12        A13        A14        A15        A16\n',
        '#Level1 (lowest)\n',
        '#Level2\n',
        '#Level3\n',
        '#Level4\n',
        '#Level5\n',
        '#Level6\n',
        '#Level7\n',
        '#Level8 (highest)\n']


def get_txt(txts):
    with open(txts[0]) as afile:
        txt_list = afile.readlines()
    with open(txts[1]) as afile:
        txt_list += afile.readlines()
    return txt_list



def get_list(line):
    alist = []
    splist = line.split(':')
    for elm in splist:
        # Regular Expression
        matched = re.match(r'\d{1,3}.\d{1,3}',elm)
        if matched:
            alist.append(matched.group())

    return alist

def get_ary(alist):
    return np.array(alist)

def calculate(ary):
    ary = ary * 0.01 * TOTAL
    return ary

def format(format_list, data_ary,ch_ary):

    data_list = []
    # modifying data(numpy) to integrate it to text file
    title = ''
    for i in range(ARRAY_NUM):
        if i==15:
            title += ('A' + str(i+1).rjust(2,'0')).rjust(10)
        else:
            title += ('A' + str(i+1).rjust(2,'0')).rjust(10)+ ','
    print(title)
    for i in range(LEVEL_NUM):
        for j in range(ARRAY_NUM):
            if j == 0:
                # ''.rjust(10):this is 10 because FORMAT use 10 words for each number.
                row_line = str(int(round(data_ary[j][i],0))).rjust(10) + ','
            else:
                row_line += str(int(round(data_ary[j][i],0))).rjust(10) + ','
        row_line = row_line[:-1] + '\n'
        print('LEVEL', str(i+1))
        print(row_line)
        data_list.append(row_line)
    output_file = open(OUT,'w')
    for i in range(int(np.ceil(len(FORMAT)))):
        if i == 0:
            output_file.write(format_list[i])
        else:
            output_file.write(format_list[i])
            output_file.write(data_list[i-1])
    output_file.close()

    return

def check_order(ch_ary):
    signal_ary = []
    order = [x for x in range(ARRAY_NUM +1)]
    for i,content in enumerate(ch_ary):
        if ch_ary[content] != None:
            num = int(ch_ary[content][-2:]) -1
            order[num] = i
            signal_ary.append(num)
    for j in range(ARRAY_NUM):
        if not j in signal_ary:
            order[j] = 16
    return order
            
    




def main():
        ## if-switch-info ##
    TEXT = 'dummy.txt'
    switch = get_switch_info(TEXT)
    CHS = ['ch01', 'ch02', 'ch03', 'ch04', 'ch05', 'ch06']
    ch_ary ={}
    for ch in CHS:
        signal_from = eval(ch+'(switch)')
        ch_ary[ch] = signal_from
        print(ch,': ',signal_from)

        ## bit-distribution ##
    ary = np.zeros((ARRAY_NUM +1,LEVEL_NUM))
    raw_list = get_txt(INPUT)
    count = 0
    for i,row in enumerate(raw_list):
        if row[0] == '!':
            ary[count] = get_ary(get_list(row))
            count +=1
    ary = calculate(ary)
       ## swap column to change RIGHT ARRAY NUMBER according to ch_ary index !!
    order = check_order(ch_ary)
    ary = ary[order,:]
    format(FORMAT,ary,ch_ary)
    print(OUT,' is saved')
    return




if __name__ == '__main__':
	main()
