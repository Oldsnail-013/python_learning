# ================== 登录验证器（学习 and 和 or） ==================

# correct_username（正确的用户名）：预设的账号，存进这个盒子里
correct_username = "admin"
# correct_password（正确的密码）：预设的密码，存进这个盒子里
correct_password = "nE7jA%5m"

# input_username（输入的用户名）：用来装用户敲的账号的盒子
input_username = input("请输入用户名：")
# input_password（输入的密码）：用来装用户敲的密码的盒子
input_password = input("请输入密码：")

# 第一关：判断用户名 并且（and） 密码是否完全匹配
# and（并且）：两边的条件必须同时成立（都为 True），结果才为 True
if input_username == correct_username and input_password == correct_password:
    # ==（比较运算符）：判断两边的值是否完全相等
    print("登录成功！欢迎回来！")
    
# 第二关：判断用户名正确，但是（and）密码错误（用 != 表示“不等于”）
# !=（不等于）：判断两边的值是否不相等
elif input_username == correct_username and input_password != correct_password:
    print("密码错误！请重试。")
    
# 第三关（兜底）：上面的都没通过，说明用户名就错了（不管密码对不对）
else:
    print("用户名不存在！")