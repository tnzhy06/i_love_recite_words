# 我爱记单词 Ver2.1
博客链接：  
https://tnzhy.top/2025/03/24/pythonjiaobenwobuaijidanciver-21/
---

## 声明
***此脚本仅为个人学习编程使用，无意实现作弊目的！***  
***使用本脚本产生的一切后果自负！***

---

## 项目介绍
本项目基于 Playwright和OpenAI SDK，实现浏览器的自动控制，题目爬取和作答。

---

## 环境要求
* Python 3.7+
* openai库
* playwright库

---

## 安装依赖
请确保安装以下依赖库， 在终端分别执行以下命令即可安装。
```bash
pip install openai
pip install playwright
playwright install chromium
```
如果安装出现错误可以改用国内镜像源安装，即在原命令后面加上 【-i 镜像源地址】，下面给出的清华大学镜像源。  
执行第三条命令如果安装速度很慢请使用科学上网或参考这篇文章换用国内镜像源。  
https://blog.csdn.net/Return_Li/article/details/136056785
```bash
pip install openai -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install playwright -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

---

## 使用方法
1. 使用支持OpenAI SDK的ai平台，我使用的是腾讯混元 https://console.cloud.tencent.com/hunyuan/ 。注册一个账号，选择【使用OpenAI SDK方式接入】，创建API Key。
2. 将代码中第12行的 \<API Key\> 替换为你的API Key。如果使用其他ai还需要修改base_url和model，具体请参考平台文档。

```bash
client = OpenAI(api_key="<API Key>", base_url="https://api.hunyuan.cloud.tencent.com/v1")
```

2. 运行脚本，根据提示输入账户密码登录“我爱记单词”。若未跳转到登录页面，请检查网络环节，关闭网络代理，使用默认的DNS。
3. 点击“开始考试”，程序会自动答题。
4. 答题完成后，会在脚本所在目录生成一个 list.json 文件，存储题目及给出的答案。  

***注意：该脚本不会自动提交试卷，请在答题结束后手动提交！！！***

