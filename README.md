# Fantia Crawler / Fantia 媒体元数据抓取工具

[English](#english) | [中文](#中文)

## English

### Project Description
A metadata crawler for organizing Fantia videos for media servers like Jellyfin and Emby. This tool helps you manage and organize video metadata from Fantia posts.

### Important Notices
- **This project does NOT provide unauthorized video downloading**
- Some Fantia posts may require membership to access metadata

### Example

> **The following are the default organization behavior, it can be changed with the "--prefix" and "--dash" flags**

#### Before Organization

```ascii
/path/to/videos/****1.mp4
/path/to/videos/****2_part1.mp4
/path/to/videos/****2_part2.mp4
/path/to/videos/****3-Kita-Ikuyo.mov
/path/to/videos/Fantia-****4 Yamada Ryo-CD1.mp4
/path/to/videos/Fantia-****4 Yamada Ryo-CD2.mp4
```

#### After Organization

```ascii
/path/to/videos/****1
├── ****1.jpg
├── ****1.mp4
└── ****1.nfo

/path/to/videos/****2
├── ****2 part1.jpg
├── ****2 part1.mp4
├── ****2 part1.nfo
├── ****2 part2.jpg
├── ****2 part2.mp4
└── ****2 part2.nfo

/path/to/videos/****3
├── ****3.jpg
├── ****3.mov
└── ****3.nfo

/path/to/videos/****4
├── ****4 CD1.jpg
├── ****4 CD1.mp4
├── ****4 CD1.nfo
├── ****4 CD2.jpg
├── ****4 CD2.mp4
└── ****4 CD2.nfo
```

#### Media Library in Jellyfin

![](https://geelao-oss.oss-cn-hangzhou.aliyuncs.com/db/202411281114496.png?x-oss-process=style/jpeg)

![](https://geelao-oss.oss-cn-hangzhou.aliyuncs.com/db/202411281114234.png?x-oss-process=style/jpeg)

### Installation
```sh
pip install fantia-crawler
```

### Usage

```bash
fantia-crawler [OPTIONS]
```

### Options
- `-e, --email`: Autofill your Fantia account email, if empty you may need to enter it manually
- `-p, --password`: Autofill your account password, if empty you may need to enter it manually
- `-b, --browser`: Can be Chrome, Edge, Firefox or Safari
- `-d, --directory`: Directory to process videos (defaults to current directory). If you are using Windows, it is recommended to surround the path with double quotes
- `-x, --prefix`: Prefix to add to organized file name. e.g., set "-x FANTIA", file and folder's name will become "FANTIA{dash}[ID]" (default: empty)
- `-D, --dash`: Define the default hypen between prefix, id and parts, default `-`

### Usage Requirements
- Video filenames must include the Fantia post ID (from URL: https://fantia.jp/posts/xxxxxxx)
- Supported video formats: .mp4 and .mov
- Accompanying image files with the same name as the video will be directly used

### Login Process
- Manual login is required to avoid anti-crawler detection
- After logging in and returning to the Fantia homepage, press Enter in the command line to continue

## 中文

### 项目描述
用于整理Fantia视频元数据的爬虫工具，帮助您将视频轻松上架到Jellyfin、Emby等媒体服务器。

### 重要声明
- **本项目不提供未经授权的视频下载**
- 部分Fantia帖子可能需要成为会员才能获取元数据
- 你的网络环境需要能够顺利访问Fantia
- 从Fantia下载预览图时，运行本项目所在的shell窗口也需要能够顺利访问Fantia

```shell
# Before using fantia-crawler

# For *nix
export HTTPS_PROXY=http://127.0.0.1:yourport
export HTTP_PROXY=http://127.0.0.1:yourport
# For Powershell
$Env:http_proxy="http://127.0.0.1:yourport";$Env:https_proxy="http://127.0.0.1:yourport"
```

### 安装
```sh
pip install fantia-crawler
```

### 使用方法

```bash
fantia-crawler [可选选项]
```

### 选项说明
- `-e, --email`: 自动填充您的 Fantia 账户邮箱，如果为空，则可能需要手动输入
- `-p, --password`: 自动填充您的账户密码，如果为空，则可能需要手动输入
- `-b, --browser`: 可以是Chrome, Edge, Firefox或者Safari
- `-d, --directory`: 处理视频的目录（默认为当前目录）。如果您使用的是 Windows 系统，建议用双引号将路径括起来
- `-x, --prefix`: 为整理后的文件名添加前缀。例如，设置为"-x FANTIA" 文件和文件夹的名称将变为 "FANTIA{dash}[ID]"（默认值为 空）
- `-D, --dash`: 定义文件各部分（前缀、Fantia Post ID号、分P）之间的连接符号，默认是`-`

### 使用要求
- 视频文件名必须包含Fantia帖子ID（来自URL: https://fantia.jp/posts/xxxxxxx）
- 支持的视频格式：.mp4 和 .mov
- 与视频文件同名的图像文件将会被直接使用，跳过爬取图片

### 登录流程
- 为避免反爬虫检测，需要手动登录。
- 在Selenium打开的页面成功登录并返回Fantia主页后，在命令行中按Enter继续
