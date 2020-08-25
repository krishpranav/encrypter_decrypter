#!usr/bin/env/python

#!usr/bin/env/python

#!usr/bin/env/python

import string
import os
from time import sleep

special_char = [
'ł',
'€',
'¶',
'ŧ',
'←',
'↓',
'→',
'ø',
'þ',
'æ',
'ß',
'ð',
'đ',
'ŋ',
'ħ',
'ĸ',
'ł',
'~',
'«',
'»',
'¢',
'“',
"'",
'µ',
'ñ',
'!',
'@',
'$',
'%',
'^',
'&',
'*',
'(',
')',
'-',
'.',
'+',
'=',
'_',
',',
'|',
'?',
'>',
'<',
'/',
'º',
'ª',
'"',
'¬',
'~',
'Ñ',
'·',
'Ł',
'{',
'}',
']',
'm',
'[',
" \ ",
'½',
'',
'\\',
'#']
numbers = [
'0',
'1',
'2',
'3',
'4',
'5',
'6',
'7',
'8',
'9']

list = list(string.ascii_letters) + numbers + special_char

def banner():
    print("Tool is created by krisna pranav")
    print("Github link https://github.com/krishpranav")
    print("Dont forget to follow me")

def encoder():
    keyinput = input('\n\033[39m \033[96mTell Your Secret : \033[1;39m')
    keyinput2 = eval(input('\n\033[39m \033[96mChoose Your Key (dont forget the key it is very important to decrypt the encrypted Secret) [1,2,3,4,5,6,7,8,9,0] : \033[1;39m'))
    sleep(2)
    code = ''
    def encoder2(message):
        j = list.index(message)
        i = (j+keyinput2)%(len(list) - 1)
        return i
    for k in keyinput:
      if k == ' ':
         code += ' '
      else:
         l = encoder2(k)
         code += list[l]
    print('\033[1;37m\n\t\t\tEncryption Is In Progress..  ')
    print("Encrypted Successfully!!")
    print("\n"+code)
    print("\n")
    options()

def decoder():
    keyinput = input('\n\033[39m \033[96mEnter Your Encrypted Text To Decrypt : \033[1;39m')
    keyinput2 = eval(input('\n\033[39m \033[96mEnter Your Old Encrypted Key To Decrypt The Text [1,2,3,4,5,6,7,8,9,0] : \033[1;39m'))
    sleep(2)
    message = ''
    for k in keyinput:
      if k == ' ':
         message += ' '
      else:
         r = list.index(k)
         l = (r - keyinput2)%(len(list) - 1)
         message += list[l]
    print('\033[1;32m\n\t\t\tDecryption Is In Progress..  ')
    print("\n"+message)
    print("\n")
    options()
def options():
    print('\n\033[39m 1)\033[96m Encrypter ')
    print('\n\033[39m 2)\033[96m Decrypter  ')
    print('\n\033[39m 3)\033[96m Exit This Tool')
    opt= int(input("\n\033[39m\033[96m Enter Your Choice : "))
    if opt == 1:
       encoder()
    elif opt == 2:
       decoder()
    else:
        banner()
        exit()

options()

