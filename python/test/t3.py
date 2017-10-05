#!/usr/bin/env python3


s1 = '4E16 754C 676F 6BCF 9694 56DB 5E74 5C31 4F1A 4E3E 884C 4E00 6B21 6BCF 6B21 D843 DC96 4E2A 7403 961F'

s1_list = s1.split()

# [print(x) for x in s1_list]

# print(' '.join(map(lambda x: '0x{}'.format(x), s1.split())))

file_name = 'uvarchar.pgc'
new_file_name = 'uvarchar_new.pgc'

with open(file_name) as f:
    lines = f.readlines()


num = len(lines)

with open(new_file_name, 'w') as wf:
    for i in range(num):
        if lines[i].lstrip().find('test("//') == 0:
            # func_name = lines[i - 2].split('')[1].strip()
            func_name = ''
            if (i > 2):
                func_name = lines[i - 2].split()[1][:-2]
                # print(lines[i].replace('test("//', 'test("{} : '.format(func_name)))
                wf.write(lines[i].replace('test("//', 'test("{} : '.format(func_name)))
        else:
            wf.write(lines[i])
        # print(lines[i].replace('test("//', func_name))

print("Finished handle {}".format(file_name))
