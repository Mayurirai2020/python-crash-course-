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
paragraph = "I am a machine learning engineer and i love the job of it and i love to do it effeciently"
# print(paragraph.upper())
# print(paragraph.lower())
# print(paragraph.title())
# print(paragraph.capitalize())
# print(paragraph.count("love"))
print(paragraph.find("love"))
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

# we use for loop for the collection of values ot the sequence or the list data type 
numbers  = range(5)#1 to 4  sequence of numbers are stored in the numbers  
for i in numbers :#then we are using the i as iterator in numbers 
    print(i) 

#change the iniatial value and 
for T in range(5,77):
    print(T)

for M in range(1,22):
    print("mayuri rai")
    print(M)
#broute force method  
for i in range(1,11):
    if i%2 == 0:
        print(i)   
for i in range(2,11,2):
    print(i) #if we start from the 2 only then step the values by the 2 then it is also the method

for i in range(1,110):
    if i % 5 == 0:
        print(i) 

for i in range(5,110,5):
    print(i)
for i in range(1,51):
    if i == 21:
        break
    if i % 3 ==0 :
        print(i)
print("you are out of the loop ")        

for g in range (1,98):
    if g==86:
        continue #it is used to skip the iteration
    if g % 6==0:
        print(g)
print("you are out the loop")     
for o in range (1,21,2):
    print(o)   
for o in range(1,20):
    if o%2 != 0:
        print(o)

for h in range(1,11):
    print (f"{h} x 57 = " ,h * 57 )
for h in range(57,571,57):
    print (f"{h} x 57 =", h )    

for k in range(1,51):
    if k == 15:
        continue
    if k % 3 == 0:
        print(k)
a = int(input("enter any number"))
b = int(input("enter another number")) 
for i in range(1, 1000):
    if i % a ==0 and i % b == 0:
        print(i)
        break 
#complex data type     
#list - collection of items, represented by the []
marks =[98,99,97,90,89, 'a',67.9]#its not necessary to have have same type in the list different data type ,
print(marks, type(marks))
print(len(marks))   
print(marks[0])
print(marks[4])
print(marks[-1])
print(marks[-2])
#slicing a list - list[starting index inclusive:ending index exclusive]
print(marks[0:2])
print(marks[-3:-1])
print(marks[-3:])#if we want value till last then we ommit like this
print(marks[:])#that means it is starting from 0 its by defalut value , complete list will be printed 
print(marks[:2])#from 0 to 2 
#loop in list 
for scores in marks :
    print(scores)
marks.append(78)#lists are mutable, we can add the values in last of the lists 
print(marks)
marks.insert(0,99)#inserting the values AT PARTICULAR  index
print(marks)
agegroup=[34,56,78,75,33,54]
print(len(agegroup))
print(agegroup[0])
print(agegroup[-1])
print(agegroup[2:6])
for ages in agegroup:
    print(agegroup)#here i printed agegroup that means list and then it printed all the lists  and here we can clearly see the conceptual difference
for ages in agegroup:#the primary usage of the for llop is traverse in the lists and tupples
    print(ages)    
 # lists in the python are mutable 
 #list_name.append/insert(the value we want to add and insert)
agegroup.insert(0,89)
agegroup.insert(9,56)
agegroup.insert(2,77)
agegroup.insert(8,99)
agegroup.insert(1,97)
agegroup.insert(4,66)
agegroup.insert(3,65)
agegroup.insert(6,63)
agegroup.insert(9,88)#in the insert it would add that values at particular index
agegroup.append(55)
agegroup.append(66)#append would add the elements in the list at the last 
print(agegroup)
#now we are checking the values exists in the list 
print(77 in agegroup)
print(55 in agegroup)
print(99 in agegroup)
print(98 in agegroup)
#now we are clearig the values in the list so we use list_nmae.clear
agegroup.clear()
print(agegroup)
print(len(agegroup))
#tuplles are immutbale - that means the cant be change 
marks2 = (22, 77,66 ,2.4, 5)
print(marks2, type(marks2))# in similar way we can access the value of the tuple
print(marks2[3])
print(marks2[2])
print(marks[1])
#operations in the tuple
#definitely the operation in the tuple that can modify the tuple cant be performed and the operations like counting the values in the tuples can be performed and knowng the index of a particular values can be performed
print(marks2.count(66))
print(marks2.count(77))
#print(marks2.count(22))
print(marks.count(66))
print(marks2.index(66))
#print(marks.index(22))#it will put that the value will not be in the list 
#also if try to put the value in the particular index 
#marks2[0]=100#it will put error because the tuples are immutable 
#its not necesary that to create the tuple we would use ()parenthesis witout it would be a tuple and if we would print the type of it , we use the ( ) to make the code readable
marks3= 77,883,8393,8
print(type(marks3))
# SET DATA TYPE - IT THE COLLECTION OF THE UNIQUE SET OF ELEMENTS 
#SET DOESNT STORE THE DUPLICATE ELEMETS 
set={11,773,33,333,11 }
print(len(set),set)
for values in set :
    print(values)
#dictionary is the collection of key and value pair and in python the value of the key is unique DICT= {KEY and VAlUE}
sgpa={"sem1":9,"sem2":9.8,"sem3":9,"sem4":9.7}
print(type(sgpa))
sgpa["sem2"]=9.92#dictionary are mutuable 






     





      
              
  

  
