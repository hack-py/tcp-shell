# tcp-shell
hacking through tcp reverse shell to dump victims data
HERE i have provided two files 

1)myser.py

its job is to create a tcp server on our system and make a connection from victim

2)mycli.py

its job is to connect to server .mycli.py is a python script so its too weird to execute a python script on target machine

next step invoves changing the mycli.py to exe(executable file) 
it involves a module importing

pyinstaller

to import it:in terminal just type

pip install pyinstaller

pyinstaller -F -w client.py

yahoo next to send the exe to target .it needs some social enginnering skills

