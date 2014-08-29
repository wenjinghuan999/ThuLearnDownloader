#-*-coding: GBK-*-
'''
@author: wensir
'''

import time
import re
import json
from thu.constants import *
from tkinter.messagebox import *
from selenium import webdriver, selenium
from selenium.common.exceptions import *
from selenium.webdriver.firefox import firefox_profile
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

class LearnBrowserNavigator(object):
    '''
    Navigate to pages of learn.tsinghua.edu.cn
    '''

    def __init__(self):
        '''
        Constructor
        '''
        MY_WEBDRIVER_PREFERENCES = "./profiles/firefox_pref.json";
        MY_WEBDRIVER_EXT = "./profiles/firefox_ext.xpi";
        class MyFirefoxProfile(FirefoxProfile):
            def __init__(self, profile_directory=None):
                with open(MY_WEBDRIVER_PREFERENCES) as default_prefs:
                    FirefoxProfile.DEFAULT_PREFERENCES = json.load(default_prefs);
                    FirefoxProfile.__init__(self, profile_directory);
            def add_extension(self, extension=MY_WEBDRIVER_EXT):
                self._install_extension(extension)
                    
        iecapabilities = {
            "browserName": "internet explorer",
            "version": "",
            "platform": "WINDOWS",
            "javascriptEnabled": True,
            "ie.ensureCleanSession": True
        }
        browsers = [{'name': STR_FIREFOX, 'enabled': USE_FIREFOX, 'driver': webdriver.Firefox, 'args': {'firefox_profile': MyFirefoxProfile()}},
                    {'name': STR_CHROME, 'enabled': USE_CHROME, 'driver': webdriver.Chrome, 'args': {}},
                    {'name': STR_IE, 'enabled': USE_IE, 'driver': webdriver.Ie, 'args': {'capabilities': iecapabilities}},
                    {'name': STR_IE_64, 'enabled': USE_IE_64, 'driver': webdriver.Ie, 'args': {'executable_path': "IEDriverServerx64.exe", 'capabilities': iecapabilities}},
                    ];
#         browsers = {STR_CHROME: webdriver.Chrome};
        for browser in browsers:
            if browser['enabled'] == 0:
                continue;
            try:
                print(STR_OPENING_BROWSER % browser['name']);
                self.browser = browser['driver'](**browser['args']);
                self.browsername = browser['name'];
                break;
            except:
                print(STR_OPEN_BROWSER_FAILED % browser['name']);
                continue;
        else:
            return None;
    
    def __del__(self):
        '''
        Destructor
        '''
        print(STR_CLOSING_BROWSER);
        self.browser.quit();
    
    def login(self, userid, userpass):
        print(STR_VISIT);
        try:
            self.browser.get(URL_LEARN);
        except:
            print(STR_ELEMENT_NOT_FOUND_ERROR);
            return None;
        self.__navtologinwindow();
        print(STR_LOGING_IN);
        while True:
            try:
                self.browser.find_element_by_name("submit1");
                break;
            except NoSuchElementException:
                pass;
        self.browser.find_element_by_name("userid").clear();
        self.browser.find_element_by_name("userid").send_keys(userid);
        self.browser.find_element_by_name("userpass").clear();
        self.browser.find_element_by_name("userpass").send_keys(userpass);
        self.browser.find_element_by_name("submit1").click();
        if self.__checkloginstate() == False:
            return None;
        while True:
            try:
                self.browser.find_element_by_class_name("text_nr2");
                break;
            except NoSuchElementException:
                pass;
        semesters_list = [];
        for link in LIST_URL_POSSIBLE_SEMESTERS:
            semester = self.__findsemester(link);
            if semester != None:
                semesters_list.append((semester['name'], link));
        return semesters_list;
    
    def selectsemester(self, link):
        semester = self.__findsemester(link);
        if semester is None:
            print(STR_ELEMENT_NOT_FOUND_ERROR);
            return None;
        element = semester['element'];
        if element is not None:
            element.click();
        time.sleep(WAITING_TIME);
        l = self.__findcourses();
        courses = [(e, e.text) for e in l];
        self.semesterpage = self.browser.current_window_handle;
        return courses;
    
    def selectcourse(self, course):
        try:
            course[0].click();
        except StaleElementReferenceException:
            print(STR_ELEMENT_NOT_FOUND_ERROR);
            return None;
        self.__navtocoursewindow();
        
    def getdownloads(self):
        self.browser.switch_to.default_content();
        while True:
            link_download = self.__findmenu(URL_DOWNLOAD);
            if link_download is not None:
                break;
        link_download.click();
        try:
            self.browser.switch_to.frame("content_frame");
        except NoSuchFrameException:
            print(STR_ELEMENT_NOT_FOUND_ERROR);
            return None;
        while True:
            try:
                self.browser.find_element_by_class_name("textTD");
            except NoSuchElementException:
                continue;
            break;
        time.sleep(WAITING_TIME);
        l = self.__finddownloads();
        files = [];
        for e in l:
            files.append(e.get_attribute("href"));
        return files;
    
    def getwares(self):
        self.browser.switch_to.default_content();
        while True:
            try:
                self.browser.find_element_by_class_name("menu_common");
            except NoSuchElementException:
                continue;
            break;
        link_ware = self.__findmenu(URL_WARE);
        if link_ware is None:
            return None;
        link_ware.click();
        try:
            self.browser.switch_to.frame("content_frame");
        except NoSuchFrameException:
            print(STR_ELEMENT_NOT_FOUND_ERROR);
            return None;
        while True:
            try:
                self.browser.find_element_by_class_name("title");
            except NoSuchElementException:
                continue;
            break;
        time.sleep(WAITING_TIME);
        l = self.__findwaredownloads();
        files = [];
        for e in l:
            files.append(e.get_attribute("href"));
        return files;
    
    def gethomeworks(self):
        self.browser.switch_to.default_content();
        while True:
            try:
                self.browser.find_element_by_class_name("menu_title");
            except NoSuchElementException:
                continue;
            break;
        link_homework = self.__findmenu(URL_HOMEWORK);
        if link_homework is None:
            return None;
        link_homework.click();
        try:
            self.browser.switch_to.frame("content_frame");
        except NoSuchFrameException:
            print(STR_ELEMENT_NOT_FOUND_ERROR);
            return -1;
        while True:
            try:
                self.browser.find_element_by_name("submit_hw");
                break;
            except NoSuchElementException:
                pass;
        time.sleep(WAITING_TIME);
        l = self.__findhomeworks();
        if l is None:
            return 0;
        else:
            return len(l);
    
    def gethomework(self, i):
        l = self.__findhomeworks();
        return (l[i], l[i].text);
    
    def gethomeworkfiles(self, homework):
        try:
            homework[0].click();
        except StaleElementReferenceException:
            print(STR_ELEMENT_NOT_FOUND_ERROR);
            return None;
        while True:
            try:
                self.browser.find_element_by_name("Submit");
                break;
            except NoSuchElementException:
                pass;
#         time.sleep(WAITING_TIME);
        l = self.__findhomeworkdownloads();
        files = [e.get_attribute("href") for e in l];
        return files;
        
#     def getbackfromhomeworkfiles(self):
#         self.browser.back();
#         while True:
#             try:
#                 self.browser.find_element_by_name("submit_hw");
#                 break;
#             except NoSuchElementException:
#                 pass;
#         time.sleep(WAITING_TIME);
    
    def closecourse(self):
        self.browser.close();
        if self.__navbacktosemesterwindow():
            try:
                self.browser.switch_to.frame("content_frame");
            except NoSuchFrameException:
                print(STR_ELEMENT_NOT_FOUND_ERROR);
                return False;
            return True;
        else:
            return False;
    
    def __checkloginstate(self):
        while True:
            try:
                alert = self.browser.switch_to.alert;
                alert_text = alert.text;
                if alert_text.startswith(STR_THULEARN_AUTH_ERROR) or alert_text.startswith(STR_THULEARN_PASS_ERROR):
                    alert.accept();
                    showerror(STR_MSGBOX_TITLE_ERROR, STR_LOGIN_FAILED % alert_text);
                    return False;
                else:
                    print(STR_ALERT_DISMISS % alert_text);
                    alert.dismiss();
                    continue;
            except NoAlertPresentException:
                try:
                    self.browser.switch_to.frame("content_frame");
                    return True;
                except NoSuchFrameException:
                    time.sleep(WAITING_TIME);
                    continue;
            
    def __findsemester(self, link):
        try:
            if link == URL_SEMESTER_CURRENT:
                l = self.browser.find_element_by_class_name(URL_SEMESTER_CURRENT);
                return {'name': l.text, 'element': None};
            else:
                l = self.browser.find_element_by_xpath('//a[contains(@href, "%s")]' % link);
                return {'name': l.text, 'element': l};
        except NoSuchElementException:
            return None;
        
    def __findmenu(self, link):
        try:
            l = self.browser.find_element_by_xpath('//a[contains(@href, "%s")]' % link);
            return l;
        except NoSuchElementException:
            return None;
        
    def __findlinks(self, link):
        try:
            l = self.browser.find_elements_by_xpath('//a[contains(@href, "%s")]' % link);
            return l;
        except NoSuchElementException:
            return None;
        
    def __findcourses(self):
        return self.__findlinks(URL_COURSES_LINK);
    
    def __finddownloads(self):
        return self.__findlinks(URL_DOWNLOADS_LINK);
    
    def __findhomeworks(self):
        return self.__findlinks(URL_HOMEWORKS_LiNK);
        
    def __findhomeworkdownloads(self):
        return self.__findlinks(URL_HOMEWORK_DOWNLOADS_LiNK);
        
    def __findwaredownloads(self):
        return self.__findhomeworkdownloads();
        
    def __navtocoursewindow(self):
        while True:
            allhandles = self.browser.window_handles;
            for h in allhandles:
                if h != self.semesterpage:
                    self.browser.switch_to.window(h);
                    return True;
        
    def __navtologinwindow(self):
        allhandles = self.browser.window_handles;
        for h in allhandles:
            self.browser.switch_to.window(h);
            if self.browser.current_url == URL_LEARN:
                return True;
        else:
            print(STR_ELEMENT_NOT_FOUND_ERROR);

    def __navbacktosemesterwindow(self):
        allhandles = self.browser.window_handles;
        for h in allhandles:
            self.browser.switch_to.window(h);
            if self.browser.current_url.endswith(URL_SEMESTER):
                return True;
        else:
            print(STR_ELEMENT_NOT_FOUND_ERROR);
            return False;
        