import os
import sys
import grp
import platform
import commands

BROWSERS = (
    'firefox',
    'chromium-browser',
    'epiphany-browser',
    'google-chrome'
)

def get_firefox():
    return commands.getstatusoutput('which firefox')[-1]

def get_chrome():
    return commands.getstatusoutput('which google-chrome')[-1]

def return_browsers():
    for browser in BROWSERS:
        code, path = commands.getstatusoutput('which %s' % browser)
        if code is 0:
            yield browser, path

def test_in_group():
    if  platform.system() == 'Linux':
        match = False
        for g in os.getgroups():
            if grp.getgrgid(g).gr_name == 'docker':
                match = True
        if match is False:
            print('User not in the docker group')
            sys.exit(1)
    return True
    
