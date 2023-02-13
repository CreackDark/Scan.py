import os

import socket

import webbrowser

from sys import stdout

from time import sleep

os.system("clear")

l= f"""\033[1;33m[\033[1;36m ✷‿✷  \033[1;33m]\033[1;36m HELLO IN MY TOOL"""        

for char in l:

         stdout.write(char)

         stdout.flush()

         sleep(0.001/0.02)    

print("")

print("")   

b = f"""\033[1;33m[\033[1;36m ✷‿✷  \033[1;33m]\033[1;32m ID ME  »»» : https://t.me/Creack_Dark"""    

for char in b:

         stdout.write(char)

         stdout.flush()

         sleep(0.001/0.02)               

webbrowser.open('https://t.me/Creack_Dark')

print('')

def banner():

    print ('\033[1;31m          ▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇         ')

    print('\033[1;31m          ▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇       ')

    print ('\033[1;31m          ▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇          ')

    print ('\033[1;31m          ▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇           ')

    print ('\033[1;31m          ▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇   \033[1;33m  CODE BY »»»» : \033[1;34mCreack_Dark')

    print ('\033[1;31m          ▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇             ')

    print ('\033[1;31m          ▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇      ')

    print ('\033[1;31m          ▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇            ')

print("")

banner()

print("")

target = str(input("\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m]\033[1;35m ENTER IP »»» : \033[1;34m"))

for p in range (1,100000):

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)را

	if r ==0:

		service = socket.getservbyport(p)

		print("")

		print("\033[1;33m[\033[1;36m ◕‿◕ \033[1;33m] \033[1;32m PORT \033[1;36m{} \033[1;34mIS OPEN »»» :\033[1;33m {}".format(p,service))

	s.close()
