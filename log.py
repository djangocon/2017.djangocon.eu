# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import csv
import sys
import re
from io import StringIO

from dateutil import parser

rx = re.compile(r'name="(.+)"')


def explode_line(line):
    row = dict()
    excluded_fields = ('csrfmiddlewaretoken',)
    fields = line.split(' ')
    datestr = fields[4].strip('[').replace('2016:', '2016 ').replace('2017:', '2017 ')
    row['created_at'] = parser.parse(datestr)
    wrapper = StringIO(line)
    d = csv.reader(wrapper, delimiter=' ', quoting=csv.QUOTE_ALL)
    for body in d:
        content = body[-1].replace('\\x0D', '').replace('\\x0A', '\n').replace('\\x22', '"')
        rows = content.split('\n')
        bound = rows[0]
        items = content.split(bound)
        for item in items:
            lines = item.strip().split('\n')
            data = rx.findall(lines[0])
            if len(data) == 1 and data[0] not in excluded_fields:
                row[data[0]] = '\n'.join(lines[1:]).strip()
    return row


def read_log(filename):
    data = []
    fieldnames = (
        'id', 'author', 'email', 'author_bio', 'created_at', 'updated_at', 'notes', 'selected', 'proposal_title',
        'proposal_abstract', 'proposal_audience', 'proposal_why', 'proposal_requirements', 'mentor_wanted',
        'mentor_offer', 'pycon'
    )
    with open(filename, 'r') as fopen:
        for line in fopen:
            data.append(explode_line(line.strip()))

    with open('proposals.csv', 'w') as fsw:
        csvf = csv.DictWriter(fsw, fieldnames=fieldnames)
        csvf.writeheader()
        csvf.writerows(data)


if __name__ == '__main__':
    read_log(sys.argv[1])
