#-*-coding: GBK-*-
'''
@author: wensir
'''

import sys
from cx_Freeze import setup, Executable

includes = ["thu.constants"];
ignores = ["readline", "win32api", "win32con"];
packages = ["thu"];
files = [("./thu/drivers/chromedriver.exe", "./drivers/chromedriver.exe"),
         ("./thu/drivers/IEDriverServer.exe", "./drivers/IEDriverServer.exe"),
         ("./thu/drivers/IEDriverServerx64.exe", "./drivers/IEDriverServerx64.exe"),
         ("./thu/profiles/firefox_pref.json", "./profiles/firefox_pref.json"),
         ("./thu/profiles/firefox_ext.xpi", "./profiles/firefox_ext.xpi"),
         ("./thu/settings.cfg", "./settings.cfg")
        ];
excludes = [];

build_exe_options = {
         "includes": includes,
         "packages": packages,
         "excludes": excludes,
         "compressed": True,
         "include_files": files
         }

setup(  name = "LearnDownloader",
        version = "1.0-beta",
        description = "Download files from learn.tsinghua.edu.cn",
        options = {"build_exe": build_exe_options},
        executables = [Executable("./thu/LearnDownloader.py")])
