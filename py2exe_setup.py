#-*-coding: GBK-*-
'''
@author: wensir
'''
from distutils.core import setup
import py2exe

includes = ["thu.constants"];
packages = ["thu"];
files = [("drivers",  
                ["./drivers/chromedriver.exe", "./drivers/IEDriverServer.exe", "./drivers/IEDriverServerx64.exe"]),
         (".",  
                ["./thu/settings.cfg"])
            ];
# excludes = ["readline", "win32api", "win32con"];
excludes = [];
options = {"py2exe":    
            {"includes": includes,
             "excludes": excludes,
             "packages": packages, 
             "bundle_files": 2
            }};
            
# setup(console=["thu/LearnDownloader.py", "thu/LearnDownloaderGui.py", "thu/constants.py", "thu/BrowserNavigator.py"]);

setup(
    options=options,
    console=["thu/LearnDownloader.py"],
    data_files=files
    );