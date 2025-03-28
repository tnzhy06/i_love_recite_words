"""
@TnZHY
这是一个用于HDU我爱记单词的答题脚本,此脚本仅供学习交流使用
项目地址 https://github.com/tnzhy06/i_love_recite_words
"""
from playwright.sync_api import sync_playwright
from openai import OpenAI
import json
import random

# <API Key>填入自己的的api
client = OpenAI(api_key="<API Key>", base_url="https://api.hunyuan.cloud.tencent.com/v1")

def get_answer(question, options):

    con = f"Question:{question}\nOptions:{options}"
    print(con)
    response = client.chat.completions.create(
        model="hunyuan-turbos-latest",
        messages=[
            {
                "role": "system",
                "content": '帮助我回答问题，user提供一个Question和4个Option，在4个Option中找出与Question相同意思相同的答案，若无意思相同的则选最相近的答案！注意每次应斟酌四个选项后再给出最佳答案。最终回答不需要解释，直接给出正确选项的大写字母并在其左右加上-,例如-A-'
            },
            {
                "role": "user",
                "content": con
            },
        ],
        stream=False
    )

    print(response.choices[0].message.content.strip())
    print()

    return response.choices[0].message.content.strip()


# 定位并点击答案
def select(page, answer):
    index_mapping = {"-A-": 1, "-B-": 2, "-C-": 3, "-D-": 4}
    xpath = f"(//div[@class='van-radio__icon van-radio__icon--round'])[{index_mapping[answer]}]"
    button = page.locator(xpath)
    button.click()

# 保存所有题目及答案到 JSON 文件
def save_to_json(questions, filename="list.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(questions, file, indent=4, ensure_ascii=False)
    print(f"Questions saved to {filename}")

# 主函数
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            user_agent="Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
            viewport={"width": 380, "height": 600},
        )
        page = context.new_page()
        page.goto("https://skl.hduhelp.com/#/english/list")

        print("已开启窗口，请登录，并于5分钟内开始考试，否则窗口将自动关闭。")
        page.wait_for_selector('.van-col.van-col--17',timeout=300000)

        # 存储所有题目信息
        questions = []

        page.wait_for_timeout(1500)

        # 循环回答问题
        for i in range(100):
            question = page.locator('.van-col.van-col--17 span:nth-of-type(2)').inner_text()
            options = [
                opt.inner_text()
                for opt in page.query_selector_all('div.van-cell')
            ]

            print(i + 1)

            correct_answer = get_answer(question, options)

            # 保存题目、选项和答案
            questions.append({
                "number": i + 1,
                "question": question,
                "options": options,
                "answer": correct_answer
            })

            if "-A-" in correct_answer:
                correct_answer="-A-"
            elif "-B-" in correct_answer:
                correct_answer = "-B-"
            elif "-C-" in correct_answer:
                correct_answer = "-C-"
            elif "-D-" in correct_answer:
                correct_answer = "-D-"
            else:
                correct_answer = random.choice(["-A-", "-B-", "-C-", "-D-"])

            select(page, correct_answer)

            # 等待一段时间以确保网页完全加载
            page.wait_for_timeout(500)

        save_to_json(questions)

        # 等待 8 分钟用于提交考卷
        print("8分钟后窗口将自动关闭。请及时提交试卷")
        page.wait_for_timeout(480000)
        browser.close()

if __name__ == "__main__":
    main()