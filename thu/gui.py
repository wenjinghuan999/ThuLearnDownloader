#-*-coding: GBK-*-
'''
@author: wensir
'''

import urllib.request
import os
import time
from stat import ST_SIZE
from tkinter import *
from tkinter.ttk import *
from tkinter.constants import *
from tkinter.messagebox import *
from thu.constants import *
from thu import browsernavigator
from progress_bar import InitBar

class LearnDownloaderGui(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.log = None;
        self.filelist = None;
        self.DOWNLOAD_ITEMS = [
                               (STR_DOWNLOADS, self.__download_downloads),
                               (STR_WARES, self.__download_wares),
                               (STR_HOMEWORKS, self.__download_homeworks),
                               ];
        os.system('cls' if os.name == 'nt' else 'clear');
        print(STR_README.replace("_", " "));
        sys.stdin.readline();
        self.showlogin();
        
    def __del__(self):
        '''
        Destructor
        '''
        del self.log;
        del self.filelist;
        
    def showlogin(self):
        self.__initgui(STR_TITLE_LOGIN, DLG_LOGIN_WIDTH, DLG_LOGIN_HEIGHT);
        win = Frame(self.root);
        win.pack(side=TOP, expand=YES, fill=NONE);
        widget_userid = Frame(win);
        widget_userpass = Frame(win);
        Label(widget_userid, text=STR_USERID_TEXT).pack(side=LEFT, expand=NO, fill=X);
        self.userid = Entry(widget_userid, state=NORMAL);
        self.userid.insert(0, USERNAME);
        self.userid.pack(side=LEFT, expand=NO, fill=X);
        Label(widget_userpass, text=STR_USERPASS_TEXT).pack(side=LEFT, expand=NO, fill=X);
        self.userpass = Entry(widget_userpass, state=NORMAL, show="*");
        self.userpass.insert(0, PASSWORD);
        self.userpass.pack(side=LEFT, expand=NO, fill=X);
        widget_userid.pack(side=TOP, expand=YES, fill=NONE);
        widget_userpass.pack(side=TOP, expand=YES, fill=NONE);
        self.btnlogin = Button(win, text=STR_BTN_LOGIN_TEXT, command=self.onclick_login);
        self.btnlogin.pack(side=BOTTOM, expand=YES, fill=NONE);
        print(STR_BEFORE_LOGIN % STR_TITLE_LOGIN);
        self.root.focus_force();
        self.root.mainloop();
    
    def onclick_login(self):
        userid = self.userid.get();
        userpass = self.userpass.get();
        self.__disablelogin();
        self.lbn = browsernavigator.LearnBrowserNavigator();
        if self.lbn is None:
            print(STR_ALL_BROWSER_FAILED);
            return None;
        semesters = self.lbn.login(userid, userpass);
        if semesters is None:
            del self.lbn;
            self.__enablelogin();
        else:
            self.__closelogin();
            self.showsemesters(semesters);
        
    def __initgui(self, title, width, height):
        self.root = Tk();
        self.root.title(title);
        self.root.resizable(False, False);
        self.root.geometry("%dx%d+%d+%d" % (width, height, (self.root.winfo_screenwidth() - width) / 2, (self.root.winfo_screenheight() - height) / 2));
        
    def __disablelogin(self):
        self.userid.config(state=DISABLED);
        self.userpass.config(state=DISABLED);
        self.btnlogin.config(state=DISABLED);
        
    def __enablelogin(self):
        self.userid.config(state=NORMAL);
        self.userpass.config(state=NORMAL);
        self.btnlogin.config(state=NORMAL);
        
    def __closelogin(self):
        del self.userid;
        del self.userpass;
        del self.btnlogin;
        self.root.destroy();
        del self.root;
        
    def showsemesters(self, semesters):
        self.__initgui(STR_TITLE_SEMESTER, DLG_SEMESTER_WIDTH, DLG_SEMESTER_HEIGHT);
        win = Frame(self.root);
        win.pack(side=TOP, expand=YES, fill=NONE);
        widget_left = LabelFrame(win, text=STR_FRAME_ITEMS);
        widget_right = LabelFrame(win, text=STR_FRAME_SEMESTER);
        self.semesters = [];
        for (name, link) in semesters:
            semester = (IntVar(), name, link);
            cb = Checkbutton(widget_right, text=name, variable=semester[0], onvalue=1, offvalue=0);
            cb.pack(side=TOP, expand=NO, fill=X);
            semester[0].set(1);
            self.semesters.append(semester);
        self.downloaditems = [];
        for (name, func) in self.DOWNLOAD_ITEMS:
            item = (IntVar(), name, func);
            cb = Checkbutton(widget_left, text=name, variable=item[0], onvalue=1, offvalue=0);
            cb.pack(side=TOP, expand=NO, fill=X);
            item[0].set(1);
            self.downloaditems.append(item);
        widget_path = Frame(win);
        Label(widget_path, text=STR_PATH_TEXT).pack(side=LEFT, expand=NO, fill=X);
        self.path = Entry(widget_path);
        self.path.insert(0, DOWNLOAD_PATH);
        self.path.pack(side=LEFT, expand=YES, fill=X);
        Button(win, text=STR_BTN_OK_TEXT, command=self.onclick_semester).pack(side=BOTTOM, expand=YES, fill=NONE);
        widget_path.pack(side=BOTTOM, expand=YES, fill=X);
        widget_left.pack(side=LEFT, expand=YES, fill=NONE);
        Label(win, text="").pack(side=LEFT, expand=YES, fill=NONE);
        widget_right.pack(side=RIGHT, expand=YES, fill=NONE);
        print(STR_BEFORE_SEMESTER % STR_TITLE_SEMESTER);
        self.root.focus_force();
        self.root.mainloop();
        
    def onclick_semester(self):
        path = self.path.get();
        try:
            path = LearnDownloaderGui.__makedirs("", path);
        except OSError:
            showerror(STR_MSGBOX_TITLE_ERROR, STR_ILLEGAL_PATH);
            return None;
        semesters = [];
        for (checkedvar, name, link) in self.semesters:
            if checkedvar.get() != 0:
                semesters.append((name, link));
        items = [];
        for (checkedvar, name, func) in self.downloaditems:
            if checkedvar.get() != 0:
                items.append(func);
        self.__closesemesters();
        self.semesters = semesters;
        self.downloaditems = items;
        self.download(path);
        
    def __closesemesters(self):
        del self.semesters;
        del self.downloaditems;
        del self.path;
        self.root.destroy();
        del self.root;
        
    def download(self, path):
        self.log = open(path + FILENAME_DOWNLOAD_LOG, "w");
        self.filelist = open(path + FILENAME_FILELIST, "w");
        starttime = time.time();
        self.filecount = 0;
        self.filesizesum = 0;
        for (name, link) in self.semesters:
            print(STR_PROCESSING_SEMESTER % name);
            courses = self.lbn.selectsemester(link);
            if courses is None:
                print(STR_ELEMENT_NOT_FOUND_ERROR);
                self.__log(LOG_SEMESTER_FAILED % name);
                continue;
            for course in courses:
                print(STR_PROCESSING_COURSE % course[1]);
                currpath = LearnDownloaderGui.__makedirs(course[1], path);
                self.__filelist(LOG_COURSE_SEP % course[1]);
                self.lbn.selectcourse(course);
                for func in self.downloaditems:
                    func(course, currpath);
                self.lbn.closecourse();
        duration = time.time() - starttime;
        os.system('cls' if os.name == 'nt' else 'clear');
        self.__log(STR_SUMMARY.replace("_", " ") % tuple(
                    list(LearnDownloaderGui.__formattime(duration)) +
                    [os.path.abspath(path)] +
                    [self.filecount] +
                    list(LearnDownloaderGui.__formatsize(self.filesizesum))
                    ));
        self.log.close();
        self.filelist.close();
        print(STR_ON_EXIT);
        sys.stdin.readline();
    
    def __download_downloads(self, course, currpath):
        files = self.lbn.getdownloads();
        if files is None:
            print(STR_ELEMENT_NOT_FOUND_ERROR);
            self.__log(LOG_DOWNLOADS_LIST_FAILED % course[1]);
            return False;
        if len(files) > 0:
            self.__filelist(LOG_ITEM_SEP % STR_DOWNLOADS);
            print(STR_DOWNLOADS);
            self.__download_files(files, currpath);
        return True;
    
    def __download_homeworks(self, course, currpath):
        n = self.lbn.gethomeworks();
        if n <= 0:
            return None;
        currpath = LearnDownloaderGui.__makedirs(STR_HOMEWORKS, currpath);
        self.__filelist(LOG_ITEM_SEP % STR_HOMEWORKS);
        i = 0;
        while i < n:
            homework = self.lbn.gethomework(i);
            print(STR_PROCESSING_HOMEWORK % homework[1]);
            files = self.lbn.gethomeworkfiles(homework);
            if files is not None and len(files) > 0:
                currcurrpath = LearnDownloaderGui.__makedirs(homework[1], currpath);
                self.__download_files(files, currcurrpath);
            nn = self.lbn.gethomeworks();
            if n < nn:
                n = nn;
            i += 1;
    
    def __download_wares(self, course, currpath):
        files = self.lbn.getwares();
        if files is None:
            print(STR_ELEMENT_NOT_FOUND_ERROR);
            self.__log(LOG_WARE_LIST_FAILED % course[1]);
            return False;
        if len(files) > 0:
            self.__filelist(LOG_ITEM_SEP % STR_WARES);
            currpath = LearnDownloaderGui.__makedirs(STR_WARES, currpath);
            print(STR_WARES);
            self.__download_files(files, currpath);
        return True;
    
    def __download_files(self, files, currpath):
        for file in files:
            filename = self.__download_file(file, currpath);
            if filename is None:
                self.__log(LOG_DOWNLOAD_FILE_FAILED % file);
            else:
                self.__filelist(filename);
    
    def __download_file(self, url, path):
        headers = [('Host', 'learn.tsinghua.edu.cn'),  
                   ('User-Agent', 'Mozilla/5.0 (Ubuntu; X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'),  
                   ('Accept', '*/*'),  
                   ('Accept-Language', 'en-us,en;q=0.5'),  
                   ('Accept-Encoding', 'gzip, deflate'),  
                   ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),  
                   ('Connection', 'keep-alive'),  
                   ('Referer', 'http://learn.tsinghua.edu.cn/MultiLanguage/lesson/student/course_locate.jsp'),
                   ('Cookie', self.__getcookie())];
        request = urllib.request.Request(url, headers=dict(headers));
        response = urllib.request.urlopen(request);
        disposition = response.getheader('Content-Disposition');
        if disposition is None:
            return None;
        length = response.getheader('Content-Length');
        if length is None or int(length) == 0:
            return None;
        length = int(length);
#         cookies = response.getheader('Set-Cookie');
#         self.__setcookie(cookies);
        filename = LearnDownloaderGui.__getstringattribute(disposition, 'filename');
        filename = filename.encode('iso-8859-1').decode('gbk');
        try:
            st = os.stat(path + filename);
            if st[ST_SIZE] == length:
                print(STR_FILE_EXISTS % filename);
                return filename;
        except FileNotFoundError:
            pass;
        (size, unit) = LearnDownloaderGui.__formatsize(length);
        print(STR_DOWNLOADING % (filename, size, unit));
        f = open(path + filename, 'wb');
        amt = 0;
        p = InitBar(title=STR_DOWNLOADING_TITLE, stream=sys.stdout);
        while amt < length:
            f.write(response.read(1024));
            amt += 1024;
            percentage = 100 * amt / length;
            p(percentage);
        del p;
            
        f.close();
        self.filecount += 1;
        self.filesizesum += length;
        return filename;
    
    def __getcookie(self):
        l = self.lbn.browser.get_cookies();
        c = {};
        for d in l:
            c[d['name']] = d['value'];
        s = "";
        for (k,v) in c.items():
            s += "%s=%s;" % (k, v);
        return s;
    
    def __setcookie(self, cookies):
        if cookies is None:
            return None;
        cookies_list = [];
        cookiestrs = cookies.split(",");
        for cookiestr in cookiestrs:
            attrstrs = cookiestr.split(";");
            attrs_list = [];
            for attrstr in attrstrs:
                kv = attrstr.split("=", 1);
                key = kv[0].strip();
                value = kv[1].strip();
                attrs_list.append((key, value));
            (name, value) = attrs_list.pop(0);
            cookie = {'name': name, 'value': value};
            for (k, v) in attrs_list:
                cookie[k] = v;
            print(cookie);
            cookies_list.append(cookie);
        for cookie in cookies_list:
            self.lbn.browser.delete_cookie(cookie['name']);
        self.lbn.browser.add_cookie(cookies_list);
    
    def __log(self, s):
        print(s);
        self.log.write(s);
        self.log.write("\n");
        
    def __filelist(self, s):
        self.filelist.write(s);
        self.filelist.write("\n");
    
    @staticmethod
    def __makedirs(dirname, path):
        dirname = dirname.replace("\\", "_");
        dirname = dirname.replace("/", "_");
        dirname = dirname.replace(":", "_");
        dirname = dirname.replace("*", "_");
        dirname = dirname.replace("?", "_");
        dirname = dirname.replace("\"", "_");
        dirname = dirname.replace("<", "_");
        dirname = dirname.replace(">", "_");
        dirname = dirname.replace("|", "_");
        path += dirname + "/";
        os.makedirs(path, exist_ok=True);
        return path;
    
    @staticmethod
    def __formatsize(size):
        for cnt in range(3):
            size /= 1024;
            if size < 1000:
                return (size, LIST_STR_UNIT[cnt]);
            
    @staticmethod
    def __formattime(time):
        hh = int(time / 3600);
        mm = int(time / 60) % 60;
        ss = int(time) % 60;
        return (hh, mm, ss);
    
    @staticmethod
    def __getstringattribute(s, attr):
        prefix = "%s=\"" % attr;
        start = s.find(prefix) + len(prefix);
        end = s.find("\"", start);
        return s[start: end];
