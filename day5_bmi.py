身高 = float(input("请输入你的身高（米）："))
体重 = float(input("请输入你的体重（公斤）"))
bmi = 体重 / (身高 * 身高) 
if bmi < 18.5:
    print("你的 BMI 是：", bmi)
    print("评级：偏瘦，建议多吃点！")
elif 18.5 <= bmi < 24:
    print("你的 BMI 是：", bmi)
    print("评级：正常，保持得不错！")
elif 24 <= bmi < 28 :
    print("你的 BMI 是：", bmi)
    print("评级：肥胖，建议关注健康！")