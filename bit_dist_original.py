import numpy as np
import re

#############################################################################
##this is a script to get bit-distribution in text/numpy format from Octad ##
#############################################################################


INPUT='./log.log'     # log-file from octad while executing Expect == raw data
TOTAL=356274688       # total number of bit
OUT='./bit_dist.txt'  # output filename, please use '.npy' or '.txt'
ARRAY_NUM=3           # number of using array
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


def get_txt(txt):
	with open(txt) as afile:
		txt_list = afile.readlines()
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

def format(format_list, data_ary):

    data_list = []
    # modifying data(numpy) to integrate it to text file
    title = ''
    for i in range(16):
        if i==15:
            title += ('A' + str(i+1).rjust(2,'0')).rjust(10)
        else:
            title += ('A' + str(i+1).rjust(2,'0')).rjust(10)+ ','
    print(title)
    for i in range(LEVEL_NUM):
        # range=16 because the maximum array number in FORMAT is 16
        for j in range(16):
            if j < ARRAY_NUM:
                if j == 0:
                    # ''.rjust(10):this is 10 because FORMAT use 10 words for each number.
                    row_line = str(int(round(data_ary[j][i],0))).rjust(10) + ','
                else:
                    row_line += str(int(round(data_ary[j][i],0))).rjust(10) + ','

            else:
                row_line += '0'.rjust(10) + ','
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



def main():
        ary = np.zeros((ARRAY_NUM,LEVEL_NUM))
        raw_list = get_txt(INPUT)
        count = 0
        for i,row in enumerate(raw_list):
            if row[0] == '!':
                ary[count] = get_ary(get_list(row))
                count +=1
        ary = calculate(ary)
        format(FORMAT,ary)
        print(OUT,' is saved')
        return




if __name__ == '__main__':
	main()
