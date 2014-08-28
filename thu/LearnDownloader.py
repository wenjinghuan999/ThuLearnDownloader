#-*-coding: GBK-*-
'''
@author: wensir
'''
import os
import sys
from thu.constants import *
from thu import BrowserNavigator, LearnDownloaderGui

if __name__ == '__main__': 
#     b = Browser();
#     b.find_link_by_href();
#     lbn = BrowserNavigator.LearnBrowserNavigator();
#     l = lbn.login('wenjh10', 'wjh19920119');
#     print(l);
    os.environ['path'] += ";" + os.path.abspath("./drivers/");
    LearnDownloaderGui.LearnDownloaderGui();
    