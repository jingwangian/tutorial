#!/usr/bin/env python3

# file_name = '/media/sf_hostshare/code.txt'

# dest_file_name = '/media/sf_hostshare/code_dest.txt'

# code_lines = []
# with open(file_name) as rf:
#     for line in rf:
#         if len(line.strip()) > 0:
#             code_lines.append(line)

# with open(dest_file_name, 'w') as wf:
#     [wf.write(x.lstrip()) for x in code_lines]

[print('test_pvar_{}();'.format(i)) for i in range(1, 13)]
print(sorted({41: 100, 1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))


s1 = 'abcdefg'

print([x for x in s1])
# print(dir(s1))
