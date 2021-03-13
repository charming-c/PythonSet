responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    #提示被调查者的名字和回答
    name = input("\nWhat is your name?")
    response = input("which mountain would you like to climb someday?")

    # 将回答存储在字典中。
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n-- Poll Result --")
for name,response in responses.items():
    print(f"{name} would like to climb {response}")