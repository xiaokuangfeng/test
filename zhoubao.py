#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

# 通知信息（企微群）
def test_text():
    # Webhook地址
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=" + "4f68fcef-c11f-4e8a-a80f-2b7ee236cff1"
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8"
    }
    # 格式为：text
    message = "质量报告填写通知："
    String_textMsg = {
        "msgtype": "text",
        "text": {"content": message + "\n\n"
                 "同学们，新的一周开始咯，记得周报！" + "\n"
                 "同学们，新的一周开始咯，记得周报！" + "\n"
                 "同学们，新的一周开始咯，记得周报！" + "\n\n"
                 "(*＾-＾*)" + "\n"
                 }
    }
    String_textMsg = json.dumps(String_textMsg)
    requests.packages.urllib3.disable_warnings()
    res = requests.post(url, data=String_textMsg, headers=HEADERS, verify=False)
    print(res.text)

if __name__=="__main__":
    test_text()
