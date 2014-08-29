#-*-coding: GBK-*-
'''
@author: wensir
'''

from ConfigObject import ConfigObject
from keyword import iskeyword

STR_OPENING_BROWSER = "���ڳ��Դ������\"%s\"...";
STR_IE = "IE";
STR_IE_64 = "IE��64λ��";
STR_CHROME = "Chrome";
STR_FIREFOX = "Firefox";
STR_CLOSING_BROWSER = "�ر������...";
STR_OPEN_BROWSER_FAILED = "��\"%s\"ʧ��";
STR_VISIT = "���ڷ�������ѧ�ã���ȴ�ҳ��������...";
STR_LOGING_IN = "���ڵ�¼...";
STR_LOGIN_FAILED = "��¼ʧ�ܣ�����ѧ����ʾ��\n%s";
STR_ALERT_DISMISS = "�����������ʾ���ڣ��ѽ���رգ���\n%s";
STR_ALL_BROWSER_FAILED = "û�п��õ���������˳�";
STR_ELEMENT_NOT_FOUND_ERROR = "���磬��������ֵ����鷢���ˡ������һ�����������벻Ҫ���� = =";
STR_PROCESSING_SEMESTER = "��ʼ����%s";
STR_PROCESSING_COURSE = "��ʼ����γ̣�%s";

STR_README = """
____==============================ʹ �� ˵ ��===============================
____|______________________________________________________________________|
____|___1. �������ܹ��Զ���������ѧ����[�γ��ļ�]��[��ѧ��Դ]�Լ�[�γ���___|
____|______ҵ]�е��ļ���___________________________________________________|
____|___2. �����򽫵���������������ء�����ǰ��ȷ��ϵͳ��װ����֧�ֵ��____|
____|______��������֧�ֵ�������У�________________________________________|
____|__________* Firefox___________________________________________________|
____|__________* Chrome____________________________________________________|
____|__________* IE����֧��IE11��__________________________________________|
____|___3. �����Կ���̨��ʽ���У����ᵯ����������[��¼]��[ѡ����Ҫ����___|
____|______������]��Ҳ���ܵ���������Ϣ���ڣ��밴��ʾ������_________________|
____|___4. �������й����У����������򿪺ܶര�ڣ��������Щ���������____|
____|______���в����������������ҳ���ڵ����ꡢ�϶��������ȡ������ܿ�____|
____|______�Խ��������С�����������ʵ���ʱ�������Ƴ���Ļ���������ܻ���____|
____|______�ٴε�����______________________________________________________|
____|___5. ������Ϣ��ο���________________________________________________|
____|__________https://github.com/wenjinghuan999/ThuLearnDownloader________|
____|______________________________________________________________________|
____========================================================================

���س�������...
""";

STR_MSGBOX_TITLE_ERROR = "������";
STR_ILLEGAL_PATH = "����·�����Ϸ������������룡";
STR_FILE_EXISTS = "�����ļ���%s";
STR_PROCESSING_HOMEWORK = "�γ���ҵ��%s";
STR_DOWNLOADING = "�����ļ���%s(%0.2f%s)";
STR_DOWNLOADING_TITLE = "������";

STR_SUMMARY = """
������ɣ�
========================

����ʱ��________%02d:%02d:%02d
�����ļ�Ŀ¼��__%s
�����ļ�������__%d
�����ļ��ܴ�С��%0.2f%s
""";
STR_ON_EXIT = """
�����ļ��б��filelist.txt
������Ϣ��download.log

���س����˳�...
""";

STR_BEFORE_LOGIN = "����\"%s\"�����������û���������";
STR_BEFORE_SEMESTER = "����\"%s\"������ѡ���������ݺ�·��";
STR_TITLE_LOGIN = "��¼";
STR_USERID_TEXT = "�û�����";
STR_USERPASS_TEXT = "��   �룺";
STR_BTN_LOGIN_TEXT = "��¼";
STR_TITLE_SEMESTER = "ѡ����Ҫ���ص�����";
STR_PATH_TEXT = "��������";
STR_BTN_OK_TEXT = "ȷ��";
STR_DOWNLOADS = "�γ��ļ�";
STR_WARES = "��ѧ��Դ";
STR_HOMEWORKS = "�γ���ҵ";
STR_FRAME_ITEMS = "������";
STR_FRAME_SEMESTER = "ѧ��";

STR_THULEARN_AUTH_ERROR = "��û�е�½����ѧ�õ�Ȩ��";
STR_THULEARN_PASS_ERROR = "�û������������";

LIST_STR_UNIT = ["KiB", "MiB", "GiB"];

LOG_SEMESTER_FAILED = "��ѧ��ҳ��ʧ�ܣ�%s";
LOG_DOWNLOADS_LIST_FAILED = "��ȡ�γ��ļ��б�ʧ�ܣ�%s";
LOG_WARE_LIST_FAILED = "��ȡ��ѧ��Դ�б�ʧ�ܣ����ģ����ܱ�����û�У���%s";
LOG_DOWNLOAD_FILE_FAILED = "�����ļ�ʧ�ܣ������Ѿ�ʧЧ�ˣ���%s";
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

print("��ȡ�����ļ�\"%s\"..." % FILENAME_CONFIG);
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
            print("�����ñ�����%s = %s" % (k, v));

