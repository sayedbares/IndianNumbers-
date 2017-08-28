# example that uses the nltk_contrib FST class
from nltk.nltk_contrib.fst.fst import *
import string
f = FST('IndianNumber')
f.add_state('1')

f.initial_state = '1'

f.add_arc('1', '1',('10'), ('das '))
f.add_arc('1', '1',('100'), ('sau ')) 
f.add_arc('1', '1',('1000'), ('hazaar '))
f.add_arc('1', '1',('100000'), ('laakh '))
f.add_arc('1', '1',('1'), ('ek ')) 
f.add_arc('1', '1',('2'), ('do ')) 
f.add_arc('1', '1',('3'), ('teen ')) 
f.add_arc('1', '1',('4'), ('chaar ')) 
f.add_arc('1', '1',('5'), ('paanch ')) 
f.add_arc('1', '1',('6'), ('chaha ')) 
f.add_arc('1', '1',('7'), ('saat ')) 
f.add_arc('1', '1',('8'), ('aath ')) 
f.add_arc('1', '1',('9'), ('nau ')) 
f.add_arc('1', '1',('11'), ('gyarah ')) 
f.add_arc('1', '1',('12'), ('barah ')) 
f.add_arc('1', '1',('13'), ('terah ')) 
f.add_arc('1', '1',('14'), ('choudah ')) 
f.add_arc('1', '1',('15'), ('pandrah ')) 
f.add_arc('1', '1',('16'), ('saulah ')) 
f.add_arc('1', '1',('17'), ('satrah ')) 
f.add_arc('1', '1',('18'), ('attharah ')) 
f.add_arc('1', '1',('19'), ('unnees '))
f.add_arc('1', '1',('20'), ('bees '))


f.set_final('1')



number = input("Please enter a number: ")
mynumber=number
count = len(str(number))-1
a=count
output=''
mynum=""
while count>0 or number!=0:
        if number==0:
            break;
        if int(number)<100:
            mynum=mynum+str(number)
            break
        else:
            if count==4 or count==3 :
                if a==3:
                    mynum=mynum+str(int(int(number)/pow(10,3)))+str(pow(10,3))
                    
                elif a>3 and count==4:
                    mynum=mynum+str(int(int(number)/pow(10,3)))+str(pow(10,3))
                
            else:
                mynum=mynum+str(int(int(number)/pow(10,count)))+str(pow(10,count))
            number=int(number)%pow(10,count)
            count=count-1

result=mynumber,'>>',''.join(f.transduce(mynum)),'\n'
result=' '.join(result)
result=str(result)
with open('outputfile.txt','a') as o:
        o.write(result)
print(result)

