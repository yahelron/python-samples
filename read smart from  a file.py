
# print only who that pass the exam (with the word P line_split[2]
f = open('inputFile.txt', 'r')
count = 0
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)

f.close()

f = open('inputFile.txt', 'r')
count = 0
for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        print(line)

f.close()