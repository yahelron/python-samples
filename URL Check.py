# Write a python script that will run forever and every 5 seconds it will
# read a url from a file called url.txt and check if it is up or not. If it is not
# up it will print “<url> is dead” and close the program


import requests
from time import sleep

while True:
    r = open("url.txt")
    url = r.readline()
    #    print(url)
    sleep(5)
    i = requests.get(url.rstrip())
    print(i)
    if i.status_code != 200:
        print(url + " is dead")
        r.close()
        # break
