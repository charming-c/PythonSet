def get_formatted_name(first_name, last_name):
    '''返回整洁的名字'''
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name

print(get_formatted_name("tomas",'edison'))
