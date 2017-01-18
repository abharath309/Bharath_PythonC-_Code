# AUTHOR BHARATH abharath@bu.edu


from decimal import Decimal,getcontext
import math
i=1
#numbers=1,2,4,8
Table = "{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
#for x in (1,2,4,8):
for x in range(1,9):
 #print ("Entering the for-loop with i value=",i,"And x value=",x)
 n=4 * int(i)
  #print(n)
 bignum=2**(2*n)-1
  #print(bignum)
  #print (bignum.bit_length()/8)
 miny=Decimal(bignum)/Decimal(2)
 #print ("miny is ",miny)
 #maxy=int(bignum)/2

 if (i==1 or i==2 or i==4 or i==8):
     print(Table.format(i,bignum,-math.ceil(miny),math.floor(miny)))
 
     #continue
 #else:
     #print ("coming out of for loop")
     
 i=i+1
 

