from time import localtime

year,month,day,hour,minute,second,_,_,_ = localtime()
print(year,month,day,hour,minute,second)
print(type(day))