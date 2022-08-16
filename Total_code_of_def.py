#1##
numbers = [3, 5, 7, 34, 2, 89, 2, 5]
m=max(numbers)
print("The maximum numbers is:-",m)
#2##
numbers = [1, 2, 3, 4, 5]
sum=0
for i in numbers:
    sum+=i
print("The sum of list is:-",sum)
#3##
unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
unorder_list.sort()
print(unorder_list)
#4##
reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
reverse_list.reverse()
print(reverse_list)
#5##
list = [8, 6, 4, 8, 4, 50, 2, 7]
min=min(list)
print("The minimum number of list:-",min)
#6##
def sum():
 print(12+13)
sum()
#7##
def welcome():
 print("Welcome to function")
welcome()
#8##
def isEven():
 if(12%2==0):
  print("Even Number")
 else:
  print("Old Number")
isEven()
#9##
def square_machine(this_list):
    i=0
    a=[]
    while i<len(this_list):
        this_list[i]=this_list[i]**2
        i+=1
    return this_list
print(square_machine([1,1,2,3,4,5,6,7,8]))
#10##
def max_of_two(x,y):
    if x>y:
        return x
    return y
def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))
print(max_of_three(24,45,67))
#11##
def multiply(numbers):
    total=1
    for i in numbers:
        total*=i
    return total
print(multiply([2,3,4,5]))
#12##
def ask_question():
    print("Who is the founder of Facebook?")
    correct_ans=1
    Option=["1 Mark Zuckerberg","2.Bill Gates","3.Steve Jobs","4.Larry Page"]
    for i in Option:
        print(i)
        ans=int(input("choose answer:-"))
        if ans==correct_ans:
            print("correct")
        else:
            print("worng")
ask_question()
#13##
def say_hello(name):
 print("Hello ", name)
 print("How are you?")
say_hello("Aatif")
#14##
numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
print (max(numbers_list))
#14##
def say_hello_language(name, language):
 if language == "hindi":
  print("Namaste ", name)
  print("Aap kaise ho?")
 elif language == "punjabi":
  print("Sat sri akaal ", name)
  print("Tuhada ki haal hai?")
 else:
  print("Hello ", name)
  print("How are you?")
say_hello_language("Rishabh", "punjabi")
say_hello_language("Armaan", "english")
say_hello_language("Abhishek", "french")
say_hello_language("Kavay", "hindi")
#15##
a=[2,5,8,9,13]
b=[4,5,9,12]
a.extend(b)
list=[]
for i in a:
    if a.count(i)<2 and i not in list:
        list.append(i)
print(list)
#16##
Numbers=[1,8,16,5,20,100]
max_number = 0
for i in Numbers:
    while i > max_number:
        max_number = i      
print(max_number)
#17##
i=int(input("enter input:-"))
i=1
while i<=2048:
    if i%2==0:
      print("true")
    else:
      print("false")
      break
#18##
def greet(names):
 for name in names:
   print("Welcome", names)
greet("Rinki")
greet("Vishal")
greet("Kartik")
greet("Bijender")
#19##
def greet(*names):
 for name in names:
  print("Welcome", names)
greet("Rinki", "Vishal", "Kartik", "Bijender")
#20##
def info(name, age):
   print(name + " is " + age + " years old")
info("Sonu","16")
info("Sana", "17")
info("Umesh", "18")
#21##
def studentDetails(name,currentMilestone,mentorName):
 print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
studentDetails("Nilam","loop","Ravi")
#22##
def function_print_line(Name,who):
  print("",Name,"\n",who)
function_print_line("my name is Abhishek","I am a Co-founder of navgurukul")
#23##
def add_number(number1,number2):
  print(number1+number2)
add_number(56,12)
#part2
def add_number_list(a,b):
  for i in range(0,len(list)):
    print(list[i]+list1[i])
list=[50, 60, 10]
list1=[10, 20, 13]
add_number_list(list,list1)
#24##
def max_of_two(x,y):
  if x>y:
    return x
  return y
def max_of_three(x,y,z):
  return max_of_two(x,max_of_two(y,z))
print(max_of_three(87,98,76))
#25##
def sum(list):
  total=0
  for i in list:
    total+=i
  return total
print(sum((8,2,3,0,7)))
#26##
def multiply(list):
  total=1
  for i in list:
    total*=i
  return total
print(multiply((8, 2, 3, -1, 7)))
#27##
def revrse_str(str):
  rstr=" "
  index=len(str)
  while index>0:
    rstr+=str[index-1]
    index=index-1
  return rstr
print(revrse_str("1234abcd"))
#28##
def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)
n=int(input("Enter the number"))
print(factorial(n))
#29##
#part 1
def check_number(a,b):
  if a%2==0 and b%2==0:
    print("Both are even")
  else:
    print("Both are not even")
check_number(4,18)
#part2
def check_number(a,b):
  for i in range(0,len(l1)):
    if (l1[i] and l2[i])%2==0:
      print("Both are even")
    else:
      print("Both are not even")
l1=[2, 6, 18, 10, 3, 75]
l2=[6, 19, 24, 12, 3, 87]
check_number(l1,l2)
#30##
def add_numbers(number_x, number_y):
 number_sum = number_x + number_y
 return number_sum

sum1 = add_numbers(20, 40)
print(sum1)
sum2 = add_numbers(560, 23)
a = 1234
b = 12
sum3 = add_numbers(a, b)
print(sum2)
print(sum3)
number_a = add_numbers(20, 40) / add_numbers(5, 1)
print(number_a)
#31##
def calculator(l1,l2):
  print("operation","*")
  for i in range(0,len(l1)):
    print(l1[i]*l2[i])
l1=[5, 10, 50, 20]
l2=[2, 20, 3, 5]
calculator(l1,l2)
#32##
def distance(kms):
  if kms < 20:
   print("close")
  elif kms < 50:
   print("median")
  else:
   Print("far")
distance(20)
#33##
def count_number(list): 
  b=[]
  for i in numbers:
    if i>=20 and i<=50:
      b.append(i)
  print(b)
  print("Number element which is greater than 20 and less than 50:-",len(b))
numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
count_number(numbers)
#34##
def max_number(list):
  print(max(list))
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
max_number(numbers)
#35#
def reverse_list(places):
  places.reverse()
  print(places)
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
reverse_list(places)
#36##
def check_palindrome(word):
  if word==word[::-1]:
    print("Palindrome")=
  else:
    print("Not Palindrome")
word=input("Enter any word:-")
check_palindrome(word)
#37##
def convert_decimal(list):
  decimal=0
  # binary_reverse()
  for i in range(len(binary_number)):
    decimal=decimal+(2**i)*binary_number[i]
    print(decimal)
binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
convert_decimal(binary_number)
#38##
def check_number(l1,l2):
  list_difference=[]
  for i in list1:
    if i not in list2:
      list_difference.append(i)
  print(list_difference)
list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
check_number(list1,list2)
#39##
def sum_of_sub_list(list):
  sum=0
  a=marks[0]
  for i in a:
    sum+=i
  b=marks[1]
  for i in b:
    sum+=i
  c=marks[2]
  for i in c:
    sum+=i
  print(sum)
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
sum_of_sub_list(marks)
#40##
def average(marks):
  sum=0
  for i in marks[0]:
    sum+=i
numbers= [10, 11, 12, 13, 14, 17, 18, 19]
sum_of_element_30(numbers)
#44##
def printPairs(arr, n, sum):
    for i in range(0, n ):
        for j in range(i + 1, n ):
            if (arr[i] + arr[j] == sum):
              print(arr[i],arr[j])
  print("Average of 1st year marks:-",sum//len(marks[0]))
  sum1=0
  for i in marks[1]:
    sum1+=i
  print("Average of 2nd year marks:-",sum1//len(marks[1]))
  total=0
  for i in marks[2]:
    total+=i
  print("Average of 3rd year marks:-",total//len(marks[2]))
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
average(marks)
#41##
def average(marks):
  sum=0
  for i in marks[0]:
    sum+=i
  print("Average of 1st year marks:-",sum//len(marks[0]))
  sum1=0
  for i in marks[1]:
    sum1+=i
  print("Average of 2nd year marks:-",sum1//len(marks[1]))
  total=0
  for i in marks[2]:
    total+=i
  print("Average of 3rd year marks:-",total//len(marks[2]))
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
average(marks)
#42##
def average(marks):
  sum=0
  for i in marks[0]:
    sum+=i
  print("Average of 1st year marks:-",sum//len(marks[0]))
  sum1=0
  for i in marks[1]:
    sum1+=i
  print("Average of 2nd year marks:-",sum1//len(marks[1]))
  total=0
  for i in marks[2]:
    total+=i
  print("Average of 3rd year marks:-",total//len(marks[2]))
  total1=0
  for i in marks[3]:
numbers= [10, 11, 12, 13, 14, 17, 18, 19]
sum_of_element_30(numbers)
#44##
def printPairs(arr, n, sum):
    for i in range(0, n ):
        for j in range(i + 1, n ):
            if (arr[i] + arr[j] == sum):
              print(arr[i],arr[j])
    total1+=i
  print("Average of 4th year marks:-",total1//len(marks[3]))
marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
average(marks)
#43##
def sum_of_element_30(list):
  number = 30
  sum=0
numbers= [10, 11, 12, 13, 14, 17, 18, 19]
sum_of_element_30(numbers)
#44##
def printPairs(arr, n, sum):
    for i in range(0, n ):
        for j in range(i + 1, n ):
            if (arr[i] + arr[j] == sum):
              print(arr[i],arr[j])
numbers= [10, 11, 12, 13, 14, 17, 18, 19]
sum_of_element_30(numbers)
#44##
def printPairs(arr, n, sum):
    list=[]
    for i in range(0, n ):
        for j in range(i + 1, n ):
            if (arr[i] + arr[j] == sum):
              list.append([arr[i],arr[j]])
    print(list)
arr = [10, 11, 12, 13, 14, 17, 18, 19]
n = len(arr)
sum = 30
printPairs(arr, n, sum)
#45##
def count(list):
  count_even=0
  count_odd=0
  sum_even=0
  sum_odd=0
  for i in range (len(elements)):
    if elements[i]%2==0:
      count_even+=1
      sum_even+=elements[i]
    else:
      count_odd+=1
      sum_odd+=elements[i]
  print("The Average of even:-",sum_even//count_even)
  print("The Average of odd:-",sum_odd//count_odd)
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
count(elements)
#46##
import collections
char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
print("original list",char_list)
ctr=collections.Counter(char_list)
print("frequency of list:-",ctr)
#47##
def duplicate(list):
  final_list=[]
  for i in n:
    if i not in final_list and n.count(i)<2:
      final_list.append(i)
  print(final_list)
n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
duplicate(n)
#48##
a="Ravindra"
for i in a:
  print(i)
  if i=="R":
    break
#49##
a=input("Enter any string:-")
print(a[False])
print(a[len(a)-len(a)])

 
