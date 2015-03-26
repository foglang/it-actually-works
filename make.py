#!/bin/python

import os, re

header = '#It actually works!\nVarious examples of the FOG language<br>2015 foglang group `github.com/foglang`\n'
# match all lines that start with something other than a '<' or a tab, and all <pre> blocks at the beginning of lines
comment_removal_regex = r'(^|\n)([^<\t\n].*|<pre>(.|\n)*?</pre>)'

with open('./README.md', 'w') as readme:
    readme.write(header)
    for dirname, dirnames, filenames in os.walk('./examples'):
        for filename in filenames:
            readme.write('##' + filename.split('.',1)[0].replace('-', ' ') + '\n')
            with open(os.path.join(dirname, filename), 'r') as source:
                readme.write(re.sub(comment_removal_regex, '', source.read()) + '\n')
