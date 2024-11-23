# 我爱记单词 Ver2.0

## 声明
**此脚本仅为个人学习编程使用，无意实现作弊目的！**
**使用本脚本产生的一切后果自负！**

---

## 项目介绍
本项目基于 Playwright和deepseek，实现题目爬取和作答和浏览器的自动控制。

---

## 安装依赖
请确保安装以下依赖库：

```bash
pip install openai
pip install playwright
playwright install
```
如果安装出现错误可以改用国内镜像源安装，具体方法自行搜索。

---

## 使用方法
1. 进入 https://www.deepseek.com 注册一个账号，获取 api_key 并将代码中 \<DeepSeek API Key\> 替换为你的 Key。
2. 运行脚本，根据提示输入账户密码登录“我爱记单词”。若未跳转到登录页面，请检查是否开启了梯子或修改了 DNS。
3. 点击“开始考试”，程序会自动答题。
4. 答题完成后，会在脚本所在目录生成一个 list.json 文件，存储题目及给出的答案。

**注意：该脚本不会自动提交试卷，请在答题结束后手动提交！！！**
