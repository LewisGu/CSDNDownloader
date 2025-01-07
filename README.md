# CSDN博客下载助手

本项目基于Python 3.6.4,所需支持包见requirements.txt,开发目的旨在提供一个便捷的，具有多种模式的CSDN博客下载工具。

搜索了一下，部分源码来自[@tansty的CSDN-spider项目](https://github.com/Tansty/CSDN-spider/)

代码本身功能还是比较丰富了，有下载单篇文章的功能，也有批量下载一个作者文章的功能。

原仓库的代码，主要不足有以下几点：
1.  博客标题无法正常解析为一级标题,代码块部分往往多两行空白
2.  面向过程，无法快速升级对每个url进行处理
3.  每个功能比较单一，未集成到一个应用中
4.  批量下载一个作者文章的模式，没有按作者分文件夹的功能
5.  没有GUI界面，人机交互比较不足

所以拟对上述几个问题进行优化，主要分具体功能代码优化、模式集成、GUI化三个部分的工作

## 2023.12.28

### v2.3.0
~~此版本为史诗级更新Bushi~~

完成了单文件模式的稳定版开发，并发布exe可执行文件


## 2022.1.6

### v2.2.1
增加了日志保存及清除的功能代码，待测试。基于os及time库，增加了几个自封装的公共小函数。
将功能代码整理到Function文件夹下
## 2022.1.5

### v2.1.0

增加了md文件名校验，解决了windows环境下文件名非法的问题。
## 2022.1.3

### v2.0.2

将requirements.txt更新为正确的版本，另外规范了README.md的格式
### v2.0

完成了文章模式的开发，即在文本框内输入单个或多个url，点击一键下载即可完成一篇或多篇博客的下载
对输入内容有校验，非法输入会有弹窗提醒

## 2022.1.2

~~我记得应该github上有这个源码的仓库，我只是做了点修改，但搜了半天发现没找到是哪个，就自己上传上来了。~~

### v1.0
功能：
1. 实现了CSDN博客的下载，能正确把博客标题解析为MD文件的一级标题

TODO List:
1.  尽量解决代码块有多余行数的问题
2.  提供多url的解析