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
STR_ALL_BROWSER_FAILED = "没有可用的浏览器，退出";
STR_ELEMENT_NOT_FOUND_ERROR = "悲剧，好像有奇怪的事情发生了。。如果一会儿程序崩了请不要惊讶 = =";
STR_PROCESSING_SEMESTER = "开始处理：%s";
STR_PROCESSING_COURSE = "开始处理课程：%s";

STR_README = \
"""
使用说明
==============================
按回车键继续...
""";

STR_MSGBOX_TITLE_ERROR = "出错啦";
STR_ILLEGAL_PATH = "下载路径不合法，请重新输入！";
STR_FILE_EXISTS = "跳过文件：%s";
STR_PROCESSING_HOMEWORK = "课程作业：%s";
STR_DOWNLOADING = "下载文件：%s(%0.2f%s)";
STR_DOWNLOADING_TITLE = "下载中";

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

FILENAME_DOWNLOAD_LOG = "download.log";
FILENAME_FILELIST = "filelist.txt";
FILENAME_CONFIG = "settings.cfg";

LIST_URL_POSSIBLE_SEMESTERS = [URL_SEMESTER_CURRENT, "MyCourse.jsp?typepage=7", "MyCourse.jsp?typepage=2"];

WAITING_TIME = 1.0;

config = ConfigObject(filename=FILENAME_CONFIG);
for section in config.sections():
    for (k,v) in config[section].items():
        k = k.upper();
        if globals().get(k) is not None and iskeyword(k) == False:
            if section.lower() == "strings":
                globals()[k] = str(v);
            elif section.lower() == "numbers":
                globals()[k] = float(v);

