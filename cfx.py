import requests
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
                                                               .x+=:.                     ..    _                    
             oec :                                            z`    ^%              x .d88"    u                     
            @88888     uL   ..         .u    .                   .   <k        u.    5888R    88Nu.   u.             
      .     8"*88%   .@88b  @88R     .d88B :@8c       .u       .@8Ned8"  ...ue888b   '888R   '88888.o888c      .u    
 .udR88N    8b.     '"Y888k/"*P     ="8888f8888r   ud8888.   .@^%8888"   888R Y888r   888R    ^8888  8888   ud8888.  
<888'888k  u888888>    Y888L          4888>'88"  :888'8888. x88:  `)8b.  888R I888>   888R     8888  8888 :888'8888. 
9888 'Y"    8888R       8888          4888> '    d888 '88%" 8888N=*8888  888R I888>   888R     8888  8888 d888 '88%" 
9888        8888P       `888N         4888>      8888.+"     %8"    R88  888R I888>   888R     8888  8888 8888.+"    
9888        *888>    .u./"888&       .d888L .+   8888L        @8Wou 9%  u8888cJ888    888R    .8888b.888P 8888L      
?8888u../   4888    d888" Y888*"     ^"8888*"    '8888c. .+ .888888P`    "*888*P"    .888B .   ^Y8888*""  '8888c. .+ 
 "8888P'    '888    ` "Y   Y"           "Y"       "88888%   `   ^"F        'Y"       ^*888%      `Y"       "88888%   
   "P'       88R                                    "YP'                               "%                    "YP'    
             88>                                                                                                     
             48                                                                                                      
             '8     
discord.gg/sniping                                                                                                              
"""

art2 = fade.fire(art)
print(art2)

def repeat():
    url = input("\033[1;37mCode\033[1m\033[1;30m$ > ")
    if url.startswith("cfx.re/join/"):
        request_url = "https://" + url
    elif url.startswith("https://cfx.re/join/"):
        request_url = url
        url = url.replace("https://", "")
    else:
        request_url = "https://cfx.re/join/" + url
        url = "cfx.re/join/" + url

    try:
        response = requests.get(request_url).headers["x-citizenfx-url"].replace("http://", "").replace("/", "")
    except requests.exceptions.RequestException as e:
        response = "might be Offline?"

    print(f"\nCFX Code: \033[1m\033[0;31m{url}")
    print(f"\x1b[0mResolved IP: \033[0;31m{response}\x1b[0m\n")
    repeat()

if __name__ == "__main__":
    repeat()
