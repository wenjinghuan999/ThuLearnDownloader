#-*-coding: GBK-*-
'''
@author: wensir
'''
from distutils.core import setup
import py2exe

includes = ["thu.constants"];
ignores = ["readline", "win32api", "win32con"];
packages = ["thu"];
files = [("drivers",
            ["./thu/drivers/chromedriver.exe", "./thu/drivers/IEDriverServer.exe", "./thu/drivers/IEDriverServerx64.exe"]),
         ("profiles",
            ["./thu/profiles/firefox_pref.json", "./thu/profiles/firefox_ext.xpi"]),
         (".",  
            ["./thu/settings.cfg"]),
        ];
# excludes = ["readline", "win32api", "win32con"];
excludes = [];
options = {"py2exe":    
            {"includes": includes,
             "ignores": ignores,
             "excludes": excludes,
             "packages": packages, 
             "bundle_files": 2,
             "compressed": True,
            }};
            
# setup(console=["thu/LearnDownloader.py", "thu/LearnDownloaderGui.py", "thu/constants.py", "thu/BrowserNavigator.py"]);

setup(
    options=options,
    console=["thu/LearnDownloader.py"],
    data_files=files
    );