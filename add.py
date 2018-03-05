import math
num1=input("enter base : ")
num2=input("enter length : ")
num3=input("enter height : ")
p=(int(num1)+int(num2)+int(num3))/2
area=math.sqrt(int(p)*int(p-num1)*int(p-num2)*int(p-num3))
print('area is %0.2i'%area)
