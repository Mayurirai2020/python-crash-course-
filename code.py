"""name = "tony Stark"
age = 53 
height = "1.83 m"
superheroname = input("enter your superhero name :")
print ("my superhero name is " + superheroname)
age = input("enter you additional age :")
new_age = int(age) + 1
print(new_age)
#age = int(age)
print (float(new_age))
print(1+69.8)#type conversion implicit 
print(1 + int(69.8))#type casting explicit"""
"""a = int(input("enter a number to be operated"))
b = int(input("enter another number to be operated"))
#operant = input ("enter the operation you wanted to perform:")
sum = a+b 
print(sum)"""
# paragraph = "I am a machine learning engineer and i love the job of it and i love to do it effeciently"
# print(paragraph.upper())
# print(paragraph.lower())
# print(paragraph.title())
# print(paragraph.capitalize())
# print(paragraph.count("love"))
# print(paragraph.find("love"))
# print(paragraph.replace("love ", "so much in love with "))
# print(paragraph.split(" "))
# print("love" in paragraph)
"""age = int(input("enter you age :"))
age = int(input("enter your age :"))
age = int(input ("enter your age :"))
name = "i am mayuri rai and i am a machine learning engineer AND I LOVE MY JOB "
print(name.upper())
print(name.lower())
print(name.find("love"))
print(name.count("love"))
print(name.title())
print(name.replace("rai","saraf"))
print(name.capitalize())
print("love" in name)

price_of_1st_product = float(input("enter price of first product"))
price_of_2nd_product = float(input("enter price of second product"))
price_of_3rd_product = float(input("enter price of third product"))
total_bill = float(price_of_1st_product + price_of_2nd_product + price_of_3rd_product)
print("total bill", total_bill )
average_price_of_the_product= ((total_bill)/2)
print("average price", average_price_of_the_product)
superheroname = input("enter the secret name of the superhero")
print(superheroname.find("s"))
print(superheroname.find("S"))
paragraph ="i am a good girls"
print(paragraph.upper())
print(paragraph.lower())
print(paragraph.find("love"))
print(paragraph.count("good"))
print(paragraph.title())
print(paragraph.capitalize())
print(paragraph.replace("good","very good"))
print("good" in paragraph)
name = input("enter your crush name")
age= input("when did you meet")
if_you_marry=print(age + str(10))
print("actually i am trying something")
print(name.lower())
print(name.find("love"))
print(name.count("love"))
print(name.title())
print(name.replace("rai","saraf"))
print(name.capitalize())
print("love" in name)

price_of_1st_product = float(input("enter price of first product"))
price_of_2nd_product = float(input("enter price of second product"))
price_of_3rd_product = float(input("enter price of third product"))
total_bill = float(price_of_1st_product + price_of_2nd_product + price_of_3rd_product)
print("total bill", total_bill )
average_price_of_the_product= ((total_bill)/2)
print("average price", average_price_of_the_product)
superheroname = input("enter the secret name of the superhero")
print(superheroname.find("s"))
print(superheroname.find("S"))
paragraph ="i am a good girls"
print(paragraph.upper())
print(paragraph.lower())
print(paragraph.find("love"))
print(paragraph.count("good"))
print(paragraph.title())
print(paragraph.capitalize())
print(paragraph.replace("good","very good"))
print("good" in paragraph)
name = input("enter your crush name")
age= input("when did you meet")
if_you_marry=print(age + str(10))
print("actually i am trying something")"""
#now seein the arthematic operations in the seen 
#operators +,-, * ,/
#operants on which the operation has been performed
print(5+6)
print(5-6)
print(5*8)
print(5/76)
print(5//76)#to get the only integer value in the 
print(7%8)# its the modulo it calculates the reaminder value modulo -- remainder
print(2 ** 5)# power operator
print(8+9)
print(9-0)
print(7*9)
print(9/8)
print(9//7)
print(6%4)
print(6**6)

#assignment operations 
x =  6
x = x + 7
x += 7
print(x)

y= 7
y = y -1

y -= 1
print(y)

z= 8
z = z*3
z *= 7
print(z)

z /= 8
z **= 7
print(z)
z %= 7
print (z)
# we use these type of operation in loops and these types of operator plays crutial role in loops like x += 1
# OPERATOR PRECEDENCE --- MORE OR LIKE BODMASS IN THE MATHS 
ans = 2 + 9 * 5 
print(ans)
yh = (2+9) *5
print(yh)
#compression operator - return the True and False 
print(6>8)
print(8<9)
print(6>=5)
print(9>=9)
print(9==9)    
print(1!=6)
#logical operators 
print(8>9 or 7<9)#OR AND NOT WORK FOR EXPRESSION AND STATEMENTS- SHOULD BE THE LOGICALL SHOULD RETURN BOOLEAN vALUES
print(8>9 and 9<=3)
print(not (7 == 8))
#conditional statements
age = 19
if age>=18 :
    print("you can vote")
    print("you can drive")
    #indentation leaving the 4 spaces in the print statement, spacing concept in python is the indetation
    #in other language there is the block of the code in curly brackets formats and in python there is the concept of indentation 
print("end of the code ")#it will execute because it is out the block

time= int(input("enter the time"))
if time>=78 :
    print("you are late")
    print("you are early to start next round")

elif time<78:
    print("you are on time")

marks=int(input("enter your marks between 0 to 100"))   
if marks >= 90 :
    print("the grade is A")
elif marks <90 and marks >= 80:
    print("the gradee is B")    
else :
    print("the grade is C")

#CALCULATOR 
a= float(input("enter the 1st  number  for operation"))
b= float(input("enter the 2nd number for the operation"))
c= input("enter the operants - +, - , *,/ , // , %, ** ") 
if c == '+':
    print(a+b)
elif c =='-':
    print(a-b)
elif c =='*':
    print(a*b)
elif c == '/':
    print(a/b)
elif c == '%':
    print(a%b)
elif c == '//':
    print(a//b)
elif c == '**':
    print(a**b)
else:
    print("output the operant services")      

#RANGE -- RETURN THE SEQUENCE OF NUMBERS FROM 0 TO THE NUMBER-1
num = range(5)  # [0,1 ,2 ,3 ,4
#range(n) # 0 to n-1 
print(num)
#if we want to print those numbers then we will use the for loop
# in range by default values start from 0 but if we want to start from some other values then we will change the by wrting the start value and stop value  
#range (start, stop ) the last stop value is not included
#also there is one more thing that is start value stop value and atep value that means by how much we have to add the numbers
#range(start, stop,step) by default start = 0 and step =1 we can change it 
 
counter = 1 
while counter<= 5:
    print(counter)
    counter += 1 #if suppose we are not adding anything to the counter then it would create infinite loop CAN BE STOP BY JUST WRITING CMD + C IN THE TERMINIAL
   
print("end")    

i = 7
while i <= 12:
    print(i)
    i +=1
print("end") 
#printing the triangle pattern
j= 1
while j<=10:
    print(j * "*")#here the string is multiplied by the integer number . the string is conatenated the j number of times 
    j += 1
print("the pattern is printed")  

m=1 
while m<=22:
    print(m * "mayurit ")
    m += 1
print("printed their r")    

n=5 
while n >0 :
    print(n * "out ")
    n -= 1
print("its out ")    


      
              
  

  
