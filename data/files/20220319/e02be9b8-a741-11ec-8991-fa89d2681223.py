

time = float(input("请输入停车小时:"))
print(type(time))
pay = 0

if time > int(time):
    pay = 5 * (int(time) + 1)
else:
    pay = 5 * int(time)


print("您的停车费为:{}".format(pay))