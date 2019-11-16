# check within log file if a password was found
import re

f = open('access.log')


log_contenet = filter(None, f.read().split('\n'))

for line in log_contenet:
    entries = re.findall(r'"([^"]*)"', line)
    url = entries[0].split(' ')[1]
    url_parts = url.split('?')
    if(len(url_parts)>1):
        query = url_parts[1]
        if (query.find('password') >-1):
            print("likely credetials found:")
            print(query)
            print("\n")