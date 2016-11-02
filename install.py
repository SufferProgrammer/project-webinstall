#!/usr/bin/python3
import sys
import os


class triggerScript():
    def __init__(self):
        os.system('start_trigger=$(find $PWD -name installer.sh) && chmod +x $start_trigger && exec $start_trigger')
        
if __name__=='__main__':
    triggerScript()