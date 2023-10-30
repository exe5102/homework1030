student = {}
student.update({'sid':input("請輸入您的學號："),                        #輸入資料
                'sname':input("請輸入您的姓名："),
                'fchina':float(input("請輸入您的國文成績：")),
                'fmath':float(input("請輸入您的數學成績：")),
                'finfo':float(input("請輸入您的電腦成績："))})
sum = student["fchina"] + student["fmath"] + student["finfo"]
avg = round(sum / 3, 2)                                         #計算

print(f'{student["sname"]}({student["sid"]})同學你好 :')        #顯示資料
print("以下是您的各科成績與分數評定\n")

print(f'國文 : {student["fchina"]}' ,end=" / ")
print(f'數學 : {student["fmath"]}' ,end=" / ")
print(f'電腦 : {student["finfo"]}')

print(f'總分 : {sum} ',end=" / ")
print(f'平均 : {avg} ')

print('------------------------')

if avg < 60:                   #輸出結果
    print("成績判定 : 不合格")
else:
    print("成績判定 : 合格")