# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("你已经成年，可以去网吧！")
# else:
#     print("你还是小朋友，回家写作业吧！")
# ================== 练习2：成绩评级器 ==================
score = int(input("请输入你的考试成绩（0-100）："))

if score >= 90:
    print("评级：A，太优秀了！")
elif score >= 80:
    print("评级：B，很不错！")
elif score >= 60:
    print("评级：C，刚刚及格，再努把力！")
else:
    print("评级：D，别灰心，好好复习！")