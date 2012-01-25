# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:12:30 2011

@author: francisco
"""
db    =    None
import time
moment = time.localtime()
    


def main():
        f = open ("jjjjj.txt", "a")
        f.write(str(time.strftime("%Y;%m;%d;%H;%M;%S;",moment)))
        f.close
    
main()
