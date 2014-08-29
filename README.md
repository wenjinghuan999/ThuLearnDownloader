清华网络学堂下载器 v1.0-beta
==
功能
--
- 批量下载网络学堂上的“课程文件”、“教学资源”和“课程作业”中的文件。
- 可以跳过同目录下已存在的、大小正确的文件。

需求
--
- Windows：需要安装以下浏览器中至少一个：
  - `Firefox`
  - `Chrome`
  - `Internet Explorer`（不支持IE11，详见下方IE用户补充说明）
- Linux & Mac：
  - 没有经过测试，并不清楚能否运行。
  - 推荐使用Firefox浏览器。使用Chrome浏览器需要安装ChromeDriver。在 http://chromedriver.storage.googleapis.com/index.html 中选择合适版本的ChromeDriver下载，将内容解压至本程序drivers文件夹即可。稍后会发Linux版和Mac版，但Mac版不会测试，you know why。

使用说明
--
- 下载zip文件，解压并运行其中的`LearnDownloader.exe`。
- 程序以控制台方式运行，但会弹出两个窗口`登录`、`选择需要下载的内容`，请按提示操作。登录时也可能弹出错误信息窗口，使用时请注意屏幕上的提示。
- 程序运行过程中，浏览器将会打开很多窗口，请勿对这些浏览器窗口进行操作，包括在浏览器页面内点击鼠标、拖动滚动条等。你可能可以将浏览器最小化，或者在适当的时机（载入页面的过程中）将其移出屏幕，但它可能还会再次弹出。
- 确保程序运行过程中浏览器不会被加入新的标签页。
- 在校外使用时，首页加载可能较慢，请耐心等待浏览器完成页面加载操作。
- 如果在下载过程中程序发生崩溃或卡死，可以结束程序并重新运行，指定相同的下载目录，已成功下载的文件将被跳过。程序崩溃或卡死的原因可能会有：
  - 网络异常导致页面加载不正常。请在网络条件较好时使用本程序。
  - 用户登录超时。当单个文件过大时，下载时间过长，可能发生用户登录超时。此时结束程序并重新运行即可。
  - 你是IE用户。（首先请参考下面的`IE用户补充说明`。但是我不保证能解决问题，不要问为什么= =）

配置文件
--
修改`settings.cfg`配置文件可以配置程序行为。可用的配置有：

### `numbers`

名称 | 值
-------|-------
WAITING_TIME | 等待时间（单位：秒）如果出现缺少文件的情况，根据网速情况适当改大。
DLG_LOGIN_WIDTH | `登录`窗口的宽度（单位：像素）如果窗口显示不全等可进行修改，默认300。
DLG_LOGIN_HEIGHT| `登录`窗口的高度（单位：像素），默认150。
DLG_SEMESTER_WIDTH| `选择需要下载的内容`窗口的宽度（单位：像素），默认400。
DLG_SEMESTER_HEIGHT| `选择需要下载的内容`窗口的高度（单位：像素）默认200。

### `strings`

名称 | 值
-------|-------
USERNAME | 用户名默认值
PASSWORD | 密码默认值
DOWNLOAD_PATH | 下载目录默认值
FILENAME_DOWNLOAD_LOG | 错误日志文件名
FILENAME_FILELIST | 下载文件列表文件名

### `boolean`

名称 | 值
-------|-------
USE_FIREFOX | 是否尝试使用Firefox浏览器（0或1）
USE_CHROME | 是否尝试使用Chrome浏览器（0或1）
USE_IE | 是否尝试使用IE浏览器（0或1）
USE_IE_64 | 是否尝试使用IE浏览器（64位驱动）（0或1）

### 示例配置文件：

```
[numbers]
WAITING_TIME = 1.0

[boolean]
USE_FIREFOX = 1
USE_CHROME = 1
USE_IE = 1
USE_IE_64 = 1

[strings]
USERNAME = wenjh10
PASSWORD = 
DOWNLOAD_PATH = C:\Some\Directory
```

IE用户补充说明
--
首先说明，本人只在Win7 + IE8上测试过，有时可以使用，但有时也会莫名其妙的崩掉或陷入死循环。其他版本可能有其他问题。IE11确定不能使用。

### 必须做的
- 更改IE安全设置（`Internet选项`-`安全`），将所有区域的安全设置恢复成默认级别（官方称应调成同一级别，但实际测试时发现必须全部是默认级别。如果失败可以尝试一下。）将四个区域的“启用保护模式”全部去掉。确定并重新启动IE。
- 确保你不是第一次运行IE，即确保启动IE时不会出现欢迎对话框。
- 确保IE启动时不会询问“是否设置为默认浏览器”。
- 确保IE启动时不会跳转至奇怪的页面，比如“您的浏览器已升级”。
- 当运行程序时，如果防火墙询问是否允许IEWebdriverServer访问网络，请允许。

### 有可能导致崩溃的因素
- 网速过慢。
- “记住密码”对话框。

### 如果你一定要尝试IE11
- 确保上述工作已经完成。
- 在注册表中添加如下键值：

32位：
```
    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE]
    "iexplore.exe"=dword:00000000
```
64位：
```
    [HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BFCACHE]
    "iexplore.exe"=dword:00000000
```
- 如果仍然不成功，我就没办法了。

已经测试的配置
--
- 可以运行
  - Win8.1 + Firefox
  - Win8.1 + Chrome
  - Win7 + Chrome
  - Win7 + IE8
- 不能运行
  - Win8.1 + IE11
