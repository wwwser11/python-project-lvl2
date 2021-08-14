#!/usr/bin/env python3
import json


def file_founder(way):
    file = json.load(open(way))
    return file


def found_difference(way1, way2):
    file1 = file_founder(way1)
    file2 = file_founder(way2)
    key_list = []
    for key in file1:
        key_list.append(key)
    for key in file2:
        key_list.append(key)
    key_list = sorted(list(tuple(key_list)))
    output = ''
    for i in key_list:
        if i in file1 and i in file2:
            new_string = ''
            if file1[i] == file2[i]:
                new_string = f'    {i}: {file1[i]}\n'
            elif file1[i] != file2[i]:
                new_string = f'  - {i}: {file1[i]}\n' \
                             f'  + {i}: {file2[i]}\n'
            if not new_string in output:
                output += new_string
        elif i in file1 and not i in file2:
            output += f'  - {i}: {file1[i]}\n'
        elif not i in file1 and i in file2:
            output += f'  + {i}: {file2[i]}\n'
            a,b = '{', '}'
    return f'{a}\n{output} {b}\n'


def output(args):
    print(found_difference(args.first_file, args.second_file))


# found_difference('/Users/Mealok/PycharmProjects/python-project-lvl2/files/file1.json',
#                  '/Users/Mealok/PycharmProjects/python-project-lvl2/files/file2.json')
