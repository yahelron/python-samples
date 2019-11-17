import os

# my_file.seek(0) or myfile.close
# try & finally, in case of error the finally will show us the error.
try:
    my_file=open("C:/Users/yahel/Desktop/11.txt", 'r', encoding='utf-8')
    print(my_file)
    for line in my_file:
        print(line)

    my_file=open("C:/Users/yahel/Desktop/1.txt", 'a+',)
    my_file.write("new text...")
    my_file.seek(0)
    my_file.read()

except IOError as e:
    print("error")
    print(e)
finally:
    print("final error")


 7.
# Create a text file named “words.txt”
# programmatically
myfile = open("words.txt", 'w+', encoding='utf-8')
print(myfile)
# 8.  Write your name into the file
myfile.write("Yahel\n")
# 9. Read your file content and print it
myfile.seek(0)
print (myfile.read())

# 10. Write Hebrew content into your text file and
# print its content programmatically.
myfile.write("כותבים עברית")
myfile.seek(0)
print(myfile.read())

# 3.  In case of error the program will stop and exit.
# absolute path may not be there (if we change computer/OS etc.)
# 4.
try:
    myfile = open("test//test.txt").read()
    print(myfile)
except FileNotFoundError as e:
    print(e, "\n Make sure path is correct")
#  5

directory = "C://test9//yaheltest"
if not os.path.exists(directory):
    os.makedirs(directory)
myfile = open(directory+"\\name.txt", 'w+',  encoding='utf-8')
myfile.write("Yahel")

#########################
# loop using a function and a sentinel
with open ("file.txt", 'r') as myfile:
    for line in iter(myfile.readline,''):
        print(line)

