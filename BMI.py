title = ('這是一個計算你BMI的程式')
print(title)
cm = input('請輸入你身高: ')
kg = input('請輸入你的體重: ')
cm = float(cm)
kg = float(kg)
cm = cm / 100
BMI = kg / (cm * cm)
print('你的BMI為: ',(BMI))
if BMI < 18.5:
	print('你的體重太輕了')
elif BMI >= 18.5 and BMI < 24:
	print('你的體重在正常範圍')
elif BMI >= 24 and BMI < 27:
	print('你的體重有點過重了')
elif BMI >= 27 and BMI < 30:
	print('你的體重屬於輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('你的體重屬於中度肥胖')
else :
	print('你已經是重度肥胖,該減肥了')