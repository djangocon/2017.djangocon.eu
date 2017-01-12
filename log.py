# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import csv
import sys
from io import StringIO

from dateutil import parser


def explode_line(line):
    row = {
        'hour': '',
        'author': '',
        'title': '',
    }
    fields = line.split(' ')
    datestr = fields[4].strip('[').replace('2016:', '2016 ').replace('2017:', '2017 ')
    row['hour'] = parser.parse(datestr)
    wrapper = StringIO(line)
    d = csv.reader(wrapper, delimiter=' ', quoting=csv.QUOTE_ALL)
    for body in d:
        content = body[-1].replace('\\x0D', '').replace('\\x0A', '\n').replace('\\x22', '"')
        rows = content.split('\n')
        bound = rows[0]
        items = content.split(bound)
        for item in items:
            lines = item.strip().split('\n')
            if 'name="proposal_title"' in lines[0]:
                row['title'] = '\n'.join(lines[1:]).strip()
            if 'name="author"' in lines[0]:
                row['author'] = '\n'.join(lines[1:]).strip()
    return row.values()


def read_log(filename):
    data = []
    with open(filename, 'r') as fopen:
        for line in fopen:
            data.append(explode_line(line.strip()))

    with open('proposals.csv', 'w') as fsw:
        csvf = csv.writer(fsw)
        csvf.writerows(data)


if __name__ == '__main__':
    read_log(sys.argv[1])
