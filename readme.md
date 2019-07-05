## 1. 项目描述

本项目基于python的flask框架，作为程序后端，实现基于深度学习的语音情绪分析功能。

前端地址：[前端](https://github.com/XLab-Tongji/sentimentAnalysisFrontend)

## 2. 安装依赖

> pip install -r requirements.txt

mac下直接运行上述命令即可。

windows如果提示no backend error，需要安装对应的音频解析工具。
> conda install -c conda-forge ffmpeg


## 3. 启动方法

在Pycharm中打开项目，运行flask_emo.py文件，启动后端。

## 4. postman测试
一个测试文件test.wav已经放置于uploads文件夹下。(命名应为英文，中文不识别）

![postman测试截图](doc/postman.jpg)

推荐使用16kHz采样率、单声道的.wav格式声音文件进行测试。




