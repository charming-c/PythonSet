# 首先，创建一个待验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_user = ['alice','brian','candace']
confirmed_user = []

# 验证每一个用户，直到没有为验证用户为止
# 将每一个经过验证的用户都移到已验证用户的列表中
while unconfirmed_user:
    current_user = unconfirmed_user.pop()

    print(f"Veryfying users:{current_user.title()}")
    confirmed_user.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for user in confirmed_user:
    print(user.title())
