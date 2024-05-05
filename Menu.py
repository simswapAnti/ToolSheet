import os
import fade
import colorama
import time
import datetime
import sys


os.system("cls")
os.system("title ATORS")
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

art2 = fade.blackwhite(art)
print(art2)
print("\033[1m\033[1;32m1. \033[1;37mResolver")
print("\033[1m\033[1;32m2. \033[1;37mPinging/Others")
print(" ")
x = input("\033[1;37mATOR\033[1m\033[1;30m$ >")

if x == "2":
    os.system("cls")
    os.system("python ping.py")
if x == "1":
    os.system("cls")
    os.system("python cfx.py")
