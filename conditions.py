# using conditional statements like if and elif. example below:
name=input('hello enter your name please')
age=input ('enter your age ')
print(name )
print(age)
if int (age) >18:
    print(f'{age} you can have your id ')
elif(int (age)<18):
    number_yearsleft= 18- int (age)
    print(f' sorry {name} you have to wait {number_yearsleft} years please')


    