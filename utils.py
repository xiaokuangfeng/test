# -*- coding: utf-8 -*-
# @Time : 2024/3/18 12:51:53
# @Author : 小狂风
# File : utils.py
# @Software : PyCharm
# utils工具包


# 读取txt文本数据
# get_text_data：把txt参数化文本中的类似于aaa,123的数据，转换为：剔除\n换行符，剔除逗号,之后的列表数据，如：[['aaa','123'],['bbb','ccc']]
def get_text_data():
    with open(r"D:\python3\project\DDT_Test\用户名和密码.txt", encoding="utf-8") as f:
        # r代表：原始字符串，字符串中的反斜杠不会被转义
        # 读取的每一行数据有换行符\n
        # 列表中的每一个数据都是字符串，不符合参数化的标准
        # 参数化的标准实参：列表中嵌套列表/元组
        # 处理数据方案：除去换行符，整理数据列表嵌套列表
        # print(f.readlines())

        list1 = []
        for i in f.readlines():
            list1.append(i.strip())  # strip：去换行符、去空格
        else:
            # print(list1)
            list2 = []
            for i in list1:
                list2.append(i.split(","))  # split：以逗号进行分割
            else:
                # print(list2) #返回符合实参的标准列表值
                return list2  # 返回符合实参的标准列表值
# print(get_text_data())  #验证方法



# 读取csv文件数据
import csv
def get_csv_data():
    c1 = csv.reader(open(r"D:\python3\project\DDT_Test\用户名和密码.csv", encoding="utf-8"))
    list1 = []
    for i in c1:
        list1.append(i)
    else:
        # print(list1)
        return list1
# print(get_csv_data()) #验证方法


# 读取excle文件
import xlrd
# 需要导入指定的xlrd版本：1.2.0
def get_excle_data():
    xls = xlrd.open_workbook(r"D:\python3\project\DDT_Test\用户名和密码.xlsx")
    print("获取工作簿")
    sheet1 = xls.sheet_by_index(0)  # 获取工作簿

    # 获取所有数据的列总数
    # print(sheet1.ncols)

    # 获取所有数据的行总数
    # print(sheet1.nrows)

    # 循环遍历：获取每一行记录
    list1 = []
    for i in range(sheet1.nrows):
        # print(sheet1.row_values(i))
        list1.append(sheet1.row_values(i))
    else:
        # print(list1)
        return list1
# print(get_excle_data()) #验证方法


# 读取json数据
import json
def get_json_data():
    # 待提取的json：data数据
    data = '''
    [
        {"name": "chengq", "sex": "男", "age": 26},
        {"name": "Alice", "sex": "男", "age": 27},
        {"name": "Tommu", "sex": "男", "age": 28}
    ]
    '''
    print(f"待提取data的格式为：", type(data))

    # #待提取的json文件
    # with open('json.data') as f:
    #     json_data = json.load(f)

    # 解析json数据
    json_data = json.loads(data)
    print(f"json_data的数据格式为：", type(json_data))

    # 打印列表元素
    list1 = []
    for i in json_data:
        list1.append(i["name"])
        list1.append(i["sex"])
        list1.append(i["age"])
    else:
        # print(list1)
        print(f"list1的数据格式为：", type(list1))
        return list1
# print(get_json_data())



# 验证码识别：
# 导包install package： baidu-aip
# 导包install package： chardet
from aip import AipOcr
def get_file_content():
    # 百度智能云秘钥
    APP_ID = '65415820'
    API_KEY = 'b15sMy4T8gZJWaBWxrAptrBt'
    SECRET_KEY = 'kAsVPNTbW9NfI6HWr7COnwWY7tu6kEtq'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    with open(r"D:\python3\project\yanzhengma_shibie\img\yanzhengma.png", "rb") as fp:
        image = fp.read()
    # 调用通用文字识别（高精度版）
    res_image = client.basicAccurate(image)
    # 开始处理res_image字典
    print(f"res_image的数据类型:", type(res_image), f"，值为：", res_image)
    # 取出字典res_image['words_result']键值
    print(f"res_image['words_result']的数据类型：", type(res_image['words_result']), f"，值为：", res_image['words_result'])
    # 取出列表res_image['words_result'][0]值
    print(f"res_image['words_result'][0]的数据类型:", type(res_image['words_result'][0]), f"，值为：", res_image['words_result'][0])
    # 取出字典res_image['words_result'][0]['words']键值
    result_code = res_image['words_result'][0]['words']
    print(f"res_image['words_result'][0]['words']的数据类型：", type(res_image['words_result'][0]['words']), f",值为：", result_code)
    # 返回验证码值
    return result_code
# print(get_file_content())
