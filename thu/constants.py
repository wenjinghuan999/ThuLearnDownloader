#-*-coding: GBK-*-
'''
@author: wensir
'''

from ConfigObject import ConfigObject
from keyword import iskeyword

STR_OPENING_BROWSER = "正在尝试打开浏览器\"%s\"...";
STR_IE = "IE";
STR_IE_64 = "IE（64位）";
STR_CHROME = "Chrome";
STR_FIREFOX = "Firefox";
STR_CLOSING_BROWSER = "关闭浏览器...";
STR_OPEN_BROWSER_FAILED = "打开\"%s\"失败";
STR_VISIT = "正在访问网络学堂，请等待页面加载完成...";
STR_LOGING_IN = "正在登录...";
STR_LOGIN_FAILED = "登录失败，网络学堂提示：\n%s";
STR_ALERT_DISMISS = "浏览器弹出提示窗口（已将其关闭）：\n%s";
STR_ALL_BROWSER_FAILED = "没有可用的浏览器，退出";
STR_ELEMENT_NOT_FOUND_ERROR = "悲剧，好像有奇怪的事情发生了。。如果一会儿程序崩了请不要惊讶 = =";
STR_PROCESSING_SEMESTER = "开始处理：%s";
STR_PROCESSING_COURSE = "开始处理课程：%s";

STR_README = """
____==============================使 用 说 明===============================
____|______________________________________________________________________|
____|___1. 本程序能够自动下载网络学堂上[课程文件]、[教学资源]以及[课程作___|
____|______业]中的文件。___________________________________________________|
____|___2. 本程序将调用浏览器进行下载。下载前请确保系统中装有受支持的浏____|
____|______览器。受支持的浏览器有：________________________________________|
____|__________* Firefox___________________________________________________|
____|__________* Chrome____________________________________________________|
____|__________* IE（不支持IE11）__________________________________________|
____|___3. 程序将以控制台方式运行，但会弹出两个窗口[登录]、[选择需要下载___|
____|______的内容]，也可能弹出错误信息窗口，请按提示操作。_________________|
____|___4. 程序运行过程中，浏览器将会打开很多窗口，请勿对这些浏览器窗口____|
____|______进行操作，包括在浏览器页面内点击鼠标、拖动滚动条等。您可能可____|
____|______以将浏览器最小化，或者在适当的时机将其移出屏幕，但它可能还会____|
____|______再次弹出。______________________________________________________|
____|___5. 更多信息请参考：________________________________________________|
____|__________https://github.com/wenjinghuan999/ThuLearnDownloader________|
____|______________________________________________________________________|
____========================================================================

按回车键继续...
""";

STR_MSGBOX_TITLE_ERROR = "出错啦";
STR_ILLEGAL_PATH = "下载路径不合法，请重新输入！";
STR_FILE_EXISTS = "跳过文件：%s";
STR_PROCESSING_HOMEWORK = "课程作业：%s";
STR_DOWNLOADING = "下载文件：%s(%0.2f%s)";
STR_DOWNLOADING_TITLE = "下载中";

STR_SUMMARY = """
下载完成！
========================

总用时：________%02d:%02d:%02d
下载文件目录：__%s
下载文件总数：__%d
下载文件总大小：%0.2f%s
""";
STR_ON_EXIT = """
下载文件列表见filelist.txt
错误信息见download.log

按回车键退出...
""";

STR_BEFORE_LOGIN = "请在\"%s\"窗口内输入用户名和密码";
STR_BEFORE_SEMESTER = "请在\"%s\"窗口内选择下载内容和路径";
STR_TITLE_LOGIN = "登录";
STR_USERID_TEXT = "用户名：";
STR_USERPASS_TEXT = "密   码：";
STR_BTN_LOGIN_TEXT = "登录";
STR_TITLE_SEMESTER = "选择需要下载的内容";
STR_PATH_TEXT = "下载至：";
STR_BTN_OK_TEXT = "确定";
STR_DOWNLOADS = "课程文件";
STR_WARES = "教学资源";
STR_HOMEWORKS = "课程作业";
STR_FRAME_ITEMS = "下载项";
STR_FRAME_SEMESTER = "学期";

STR_THULEARN_AUTH_ERROR = "您没有登陆网络学堂的权限";
STR_THULEARN_PASS_ERROR = "用户名或密码错误";

LIST_STR_UNIT = ["KiB", "MiB", "GiB"];

LOG_SEMESTER_FAILED = "打开学期页面失败：%s";
LOG_DOWNLOADS_LIST_FAILED = "获取课程文件列表失败：%s";
LOG_WARE_LIST_FAILED = "获取教学资源列表失败（别担心，可能本来就没有）：%s";
LOG_DOWNLOAD_FILE_FAILED = "下载文件失败（可能已经失效了）：%s";
LOG_COURSE_SEP = "\n==========%s==========\n";
LOG_ITEM_SEP = "******%s******";

URL_LEARN = "http://learn.tsinghua.edu.cn/";
URL_SEMESTER = "mainstudent.jsp";
URL_DOWNLOAD = "/MultiLanguage/lesson/student/download.jsp?course_id=";
URL_HOMEWORK = "/MultiLanguage/lesson/student/hom_wk_brw.jsp?course_id=";
URL_WARE = "/MultiLanguage/lesson/student/ware_list.jsp?course_id=";
URL_SEMESTER_CURRENT = "active_on";
URL_COURSES_LINK = "/MultiLanguage/lesson/student/course_locate.jsp?course_id=";
URL_DOWNLOADS_LINK = "/uploadFile/downloadFile_student.jsp";
URL_HOMEWORKS_LiNK = "hom_wk_detail.jsp";
URL_HOMEWORK_DOWNLOADS_LiNK = "/uploadFile/downloadFile.jsp";

LIST_URL_POSSIBLE_SEMESTERS = [URL_SEMESTER_CURRENT, "MyCourse.jsp?typepage=7", "MyCourse.jsp?typepage=2"];

###### config ######

FILENAME_DOWNLOAD_LOG = "download.log";
FILENAME_FILELIST = "filelist.txt";
FILENAME_CONFIG = "settings.cfg";

WAITING_TIME = 1.0;

DLG_LOGIN_WIDTH = 300;
DLG_LOGIN_HEIGHT = 150;
DLG_SEMESTER_WIDTH = 400;
DLG_SEMESTER_HEIGHT = 200;

USE_FIREFOX = 1;
USE_CHROME = 1;
USE_IE = 1;
USE_IE_64 = 1;

USERNAME = "";
PASSWORD = "";
DOWNLOAD_PATH = "";

print("读取配置文件\"%s\"..." % FILENAME_CONFIG);
config = ConfigObject(filename=FILENAME_CONFIG);
for section in config.sections():
    for (k,v) in config[section].items():
        k = k.upper();
        if globals().get(k) is not None and iskeyword(k) == False:
            if section.lower() == "strings" and str(type(globals()[k])) == "<class 'str'>":
                globals()[k] = str(v);
            elif section.lower() == "numbers" and (str(type(globals()[k])) == "<class 'float'>" or str(type(globals()[k])) == "<class 'int'>"):
                globals()[k] = float(v);
            elif section.lower() == "boolean" and str(type(globals()[k])) == "<class 'int'>":
                globals()[k] = int(v);
            else:
                continue;
            print("已设置变量：%s = %s" % (k, v));

