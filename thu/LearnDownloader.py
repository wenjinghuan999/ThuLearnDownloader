#-*-coding: GBK-*-
'''
@author: wensir
'''
import os
import sys
from thu.constants import *
from thu import browsernavigator
from thu import gui

if __name__ == '__main__': 
#     b = Browser();
#     b.find_link_by_href();
#     lbn = browsernavigator.LearnBrowserNavigator();
#     l = lbn.login('wenjh10', 'wjh19920119');
#     print(l);
    os.environ['path'] += ";" + os.path.abspath("./drivers/");
    gui.LearnDownloaderGui();
    