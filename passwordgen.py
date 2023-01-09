#import the modules random, string & re - regular expression
import random
import string
import re


print('\n \t\t Created by YASH INGLE \t ')
print('\n Hello, Welcome to Password generator!')

#input the length of password
length = int(input ('\n Enter the length of password (MINIMUM 8 length characters): '))

print('\n Enter words or digits or symbol (#,$,@,%) or combination BELOW!! \n Greater or equal to the length of password ')

#1 Get the input from the user

word = input('\n Enter the words/digits/symbol: ')


# 2 use random to generate the password
temp = random. sample(word, length)

#create the password
password = "". join(temp)

#print the password
print('\n Your',"",length,'length paswword is: ',password)


#3 check the strength of the Password

if(len(password)>=8):

    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',password))==True):
        print("\n The generated password is strong")
        print(" Password copy is successfully exported in Password.txt file ")
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',password))==True):
        print("\n The generated password is weak")
        print(" Password copy is successfully exported in Password.txt file ")

else:
    print("\n You have entered an invalid password.")


#4 write the password into the file
lines = ['Random Password generated using Python is:\n ']
with open('Password.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write(password)
