#!/usr/bin/env python3
"""
Design Lib - 邮件发送工具
用于赞助商联系、用户通知、平台注册等

Usage:
    python3 email_sender.py --to "recipient@example.com" --subject "主题" --body "内容"
    python3 email_sender.py --to "recipient@example.com" --template "sponsor_reply" --vars '{"name":"张三"}'
"""

import smtplib
import argparse
import json
import os
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# QQ邮箱 SMTP 配置
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 465
SENDER_EMAIL = "weta_zheng@qq.com"
AUTH_CODE = "swovidbgrsthebfb"

# 邮件模板
TEMPLATES = {
    "sponsor_reply": {
        "subject": "【Design Lib】感谢您对我们的关注！",
        "body": """{name}，您好！

感谢您对 Design Lib 的关注！

我们是一个AI友好的前端设计组件库，为开发者和AI编程工具提供高质量、可复用的UI组件。

📋 我们的组件库：http://101.37.166.208:11930
🤝 赞助方案：http://101.37.166.208:11930/sponsor

如果您有任何问题或合作意向，请随时回复此邮件。

祝好，
Design Lib 团队
weta_zheng@qq.com"""
    },
    "sponsor_welcome": {
        "subject": "【Design Lib】欢迎成为赞助商！",
        "body": """{name}，您好！

欢迎成为 Design Lib 的赞助商！

您的赞助对我们非常重要，这将帮助我们：
- 持续扩充高质量组件库
- 为更多开发者和AI工具提供服务
- 保持项目免费、开源

我们会在3个工作日内完成赞助位的配置和上线。

如有任何问题，请随时联系。

祝好，
Design Lib 团队"""
    },
    "weekly_update": {
        "subject": "【Design Lib】本周更新报告",
        "body": """大家好！

这是 Design Lib 本周的更新摘要：

{content}

🌐 查看完整组件库：http://101.37.166.208:11930
⭐ GitHub：https://github.com/zhengyehui/my-design-lib

祝好，
Design Lib 团队"""
    }
}


def send_email(to_email, subject, body, is_html=False):
    """发送邮件"""
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"Design Lib <{SENDER_EMAIL}>"
        msg["To"] = to_email

        if is_html:
            msg.attach(MIMEText(body, "html", "utf-8"))
        else:
            msg.attach(MIMEText(body, "plain", "utf-8"))

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, timeout=30) as server:
            server.login(SENDER_EMAIL, AUTH_CODE)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())

        # 记录发送日志
        log_entry = {
            "time": datetime.now().isoformat(),
            "to": to_email,
            "subject": subject,
            "status": "success"
        }
        log_file = os.path.join(os.path.dirname(__file__), "..", "data", "email_log.jsonl")
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

        print(f"✅ 邮件发送成功 → {to_email}")
        return True

    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")
        return False


def send_template(to_email, template_name, vars_dict=None):
    """使用模板发送邮件"""
    if template_name not in TEMPLATES:
        print(f"❌ 未知模板: {template_name}")
        print(f"   可用模板: {', '.join(TEMPLATES.keys())}")
        return False

    tpl = TEMPLATES[template_name]
    vars_dict = vars_dict or {}

    subject = tpl["subject"]
    body = tpl["body"].format(**vars_dict)

    return send_email(to_email, subject, body)


def main():
    parser = argparse.ArgumentParser(description="Design Lib 邮件发送工具")
    parser.add_argument("--to", help="收件人邮箱")
    parser.add_argument("--subject", help="邮件主题")
    parser.add_argument("--body", help="邮件内容")
    parser.add_argument("--template", help="使用预设模板")
    parser.add_argument("--vars", help="模板变量 (JSON格式)")
    parser.add_argument("--html", action="store_true", help="HTML格式邮件")
    parser.add_argument("--test", action="store_true", help="发送测试邮件到自己")
    args = parser.parse_args()

    if args.test:
        # 发送测试邮件到自己
        return send_email(
            SENDER_EMAIL,
            "【Design Lib】邮件系统测试",
            f"这是一封测试邮件，发送时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n如果你收到了这封邮件，说明邮件系统配置正确！"
        )

    if not args.to:
        print("❌ 请指定收件人 --to")
        sys.exit(1)

    if args.template:
        vars_dict = json.loads(args.vars) if args.vars else {}
        return send_template(args.to, args.template, vars_dict)

    if args.subject and args.body:
        return send_email(args.to, args.subject, args.body, args.html)

    print("❌ 请提供 --subject + --body 或 --template")
    sys.exit(1)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
