import os
import json
ab = {}  # 通信录保存在字典中name:tel
# 从JSON文件中读取通信录
if os.path.exists("addressbook.json"):
    with open('addressbook.json', 'r+', encoding='utf-8') as f:
        ab = json.load(f)
        flag = True

        while flag:
            print('|---欢迎使用通讯录程序---｜\n'
                '|---1: 显示通讯录清单---｜\n'
                '|---2: 查询联系人资料---｜\n'
                '|---3: 插入新的联系人---｜\n'
                '|---4: 删除已有联系人---｜\n'
                '|---0: 退出-----------｜\n')
            choice = input('请选择功能菜单（0-4）:')
            choice = int(choice)
            if choice == 1:
                for k, v in ab.items():
                    print(f"{k}:{v}")

            elif choice == 2:
                name = input("请输入名字:")
                for k, v in ab.items():
                    if k == name:
                        print(f"{k}:{v}")

            elif choice == 3:
                n = input("请输入要保存的联系人姓名:")
                m = int(input("请输入要保存的联系人号码:"))
                ab[n] = m
                f.write(str(ab))

            elif choice == 4:
                name = input("请输入名字:")
                del ab[name]
                
            elif choice == 0:
                flag = False

            else:
                continue
