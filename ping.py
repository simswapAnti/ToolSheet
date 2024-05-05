import socket
import os
import fade
import colorama
import time
import random

os.system("cls")
os.system("title ATORS")

# ASCII Art
art = """
.
.
                               s       .            s                                  ..    .x+=:.   
                              :8      @88>         :8                            x .d88"    z`    ^%  
               u.    u.      .88      %8P         .88           u.          u.    5888R        .   <k 
      u      x@88k u@88c.   :888ooo    .         :888ooo  ...ue888b   ...ue888b   '888R      .@8Ned8" 
   us888u.  ^"8888""8888" -*8888888  .@88u     -*8888888  888R Y888r  888R Y888r   888R    .@^%8888"  
.@88 "8888"   8888  888R    8888    ''888E`      8888     888R I888>  888R I888>   888R   x88:  `)8b. 
9888  9888    8888  888R    8888      888E       8888     888R I888>  888R I888>   888R   8888N=*8888 
9888  9888    8888  888R    8888      888E       8888     888R I888>  888R I888>   888R    %8"    R88 
9888  9888    8888  888R   .8888Lu=   888E      .8888Lu= u8888cJ888  u8888cJ888    888R     @8Wou 9%  
9888  9888   "*88*" 8888"  ^%888*     888&      ^%888*    "*888*P"    "*888*P"    .888B . .888888P`   
"888*""888"    ""   'Y"      'Y"      R888"       'Y"       'Y"         'Y"       ^*888%  `   ^"F     
 ^Y"   ^Y'                             ""                                           "%                
discord.gg/sniping                                                                                          
                                                                                                      
                                                                                                      
"""
art2 = fade.purpleblue(art)
print(art2)

def random_color():
    return random.choice([colorama.Fore.RED, colorama.Fore.GREEN, colorama.Fore.YELLOW, colorama.Fore.BLUE, colorama.Fore.MAGENTA, colorama.Fore.CYAN])

def tcp_ping(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2) 
    try:
        s.connect((host, port))
        start = time.time()
        s.send(b'ping')
        s.recv(1024)
        end = time.time()
        elapsed = round((end - start) * 1000) 
        print(f"{random_color()}{host}:{port} - Ping {elapsed}ms - still online :({colorama.Style.RESET_ALL}")
    except (socket.timeout, ConnectionRefusedError):
        print(f"{colorama.Fore.RED}{host}:{port} - slammed by the big don nigger{colorama.Style.RESET_ALL}")
    finally:
        s.close()

def ping_multiple_times(host, port, count):
    for _ in range(count):
        tcp_ping(host, port)
        time.sleep(1) 

host = input("Enter IP address to ping: ")
port = int(input("Enter port to ping: "))
count = int(input("Enter number of times to ping: "))
ping_multiple_times(host, port, count)
