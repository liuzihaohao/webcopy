# webcopy

## 开发目的
当下互联网已融入到每个人的生活之中，而随着互联网的发展，人们有了 使用互联网进行沟通的需求，这时就出现了各种的即时网络通信软件，而这些软件有一些弊端
1.	用户需要注册和登录
2.	用户发送的文件不可太大
3.	如果发的是视频、音频、图片 软件会放弃清晰度
4.	用户如果要使用则必须下载应用
5.	可能会泄露个人隐私
6.	因为用户容易遗忘自己存的信息，导致没有及时删除无用数据文件，服务端会存许多用户不需要的数据文件
这样就需要有一个可以解决以上问题的方案，而我就制作了一个名为"云分享"的网站，此网站拥有以下几点优点
1.	用户使用不需要注册和登录，使用户可以拥有更多时间注重内容，同时也减少了用户隐私的泄露
2.	这个解决方案为网站所以用户不需要下载任何其他应用只需一个浏览器就可以使用该应用
3.	这个网站不会对视频、音频、图片 进行任何压缩，保证了文件不会被更改
4.	此网站采用阅后即焚措施，既保护了用户的隐私，也保证了服务器不会存储无用信息文件
5.	此网站源码已经开源在gitee且代码清晰易读，模块性强便于进行二次开发
希望这个项目能切实际地使同学们可以便捷地与朋友分享自己的数据
## 项目环境
此项目使用了Python3.8(计算机编程语言)和Django3.2(Python Web MTV框架)进行了网站后端的开发
而前端则使用了Html5(超文本标记语言),CSS(层叠样式表)和Javascript(解释型编程语言)以及Bootstrap(前端开发框架)等技术来实现

## 项目部署
1.	解压代码文件压缩包webcopy.zip
2.	在联网环境下双击python-3.8.5-amd64-webinstall.exe 以安装Python依赖(电脑中已有的不用安装,但需保证Python 版本为3.8 及以上)
3.	进入 webcopy 文件夹，打开命令提示符
4.	在联网环境下输入 pip install -r requirements.txt 安装库依赖
5.	输入 python manage.py makemigrations 进行迁移
6.	输入 python manage.py migrate生成数据库
7.	输入 python manage.py runserver 80 运行网站(runserver默认端口为8000,这里更改为80)
如果要备份数据库,需要将db.db 和media/ 下的所有文件 进行备份
## 使用方法
文字分享功能可以让你将一些文字便捷地分享给别人，或在其他设备上获取内容。 首先，先找到“分享文字”，然后在大输入框中输入自己想要分享的文字，写完后再点击提交按钮，信息会被提交上去  而页面会被重定向到另一个页面。 这个界面顶上会有一个黄色的提示框，里面为你提供了两种分享的方式，你可以将信息对应的代码给别人，别人就可在页面顶端的提取功能，提取出你 分享的文字，你也可以点击复制按钮，将复制的链接发送给别人，别人通过访问链接来查看你提交的内容。  
文件分享功能可以让你将文件便捷地分享给别人，或在其他设备上获取文件。 首先，先找到“分享文件”，然后点击浏览，选中一个非空的文件，点击提交按钮，文件会被提交上去，而页面会被重定向到另一个页面。 这个页面顶上会有一个黄色的提示框，里面为你提供了两种分享的方式，你可以将信息对应的代码给别人，别人就可在页面顶端的提取功能，提取出你 分享的文件，你也可以点复制按钮，将复制的链接发送给别人，别人通过访问链接来查看你提交的文件。
 
如何查看其他人分享给你的文字或文件？首先，在页面的顶端会有一个小输入框，输入别人给你的分享码，点击旁边的蓝色提交按钮。 
页面会被重定向到另一个页面。 这个页面上会有别人上传的文字或下载按钮，取决于别人上传的是文字还是文件，如果要关闭则点击一下黑色背景即可。

## 具体文档可以查看 [docs.pdf](https://github.com/liuzihaohao/webcopy/raw/main/docs.pdf)
