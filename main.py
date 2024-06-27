#PROGRAMING TASK FOR REFRESHER
###########  1  ##############
#Calculate the Area of a Rectangle:

#Input:
#Enter the length of the rectangle: 5
#Enter the width of the rectangle: 3


length = 5
width = 3
Area = length * width
print("the Area of Rectangle is",Area)

############# 2 ###########
#Check if a Number is Even or Odd:

NUMBER = int(input
             ("your number:")
             )
if NUMBER % 2==0:
    print("your number is even buddy")
else:
    ("its an odd number dude") 



########## 3 ########
##Reverse a String:

original_string = "umer here"
reversed_string = original_string[::-1]  #-1 is use forreading the text from backward

print("Original string:", original_string)
print("Reversed string:", reversed_string)



###### 4 #######
## Find the Factorial of a Number:
def fact(u):
    if u == 0:  ##its a base case(stops the recursion)
        return 1
    else:      ##its an recursive case(solve program step by step)
        return u * fact(u - 1)
number = 6
result = fact(number)
print("The factorial of", number, "is:", result)




###### 5 #######
# Find the larger among three number:
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

if a >= b and a >= c:
    print("The first is the largest number among", a,",",b ,", and", c, "is", a)
elif b >= a and b >= c:
    print("The second is the largest number among", a, ",", b, ", and", c,"is", b)
else:
    print("The third is the largest number among", a,  b, ", and", c, "is:", c)



####### ^6 #######
## convert celcius into fahrenheit
celsius = float(input("enter temperature in celsius"))
fahrenheit=(celsius *9/5)+ 32
print(f"{celsius}C is equal to {fahrenheit}F")



####### 7#######
#### leap year


def leapyear(year):
    if year % 4 == 0:
        if year % 400 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else :
        return False
            

year = 2022
if leapyear(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
    
    
    ######*8##########
### fibiancio series
firstnumber= 0
secondnumber=1
for i in range(1,15):
    print(firstnumber)
    thirdnumber=firstnumber + secondnumber
    firstnumber=secondnumber
    secondnumber=thirdnumber


#####PRogramming Challenges


########1#########

## find meadian of three number
def medain(a, b, c):
    if (a <= b and a >= c) or (a >= b and a <= c): ##(agr a lesser ya barabar b k and a greater than ya babar c k)
        return a                                   ##agr a greater ya barabar b k and a lesser than ya babar c k)
    elif (b <= a and b >= c) or (b >= a and b <= c):
        return b
    else:
        return c

a, b, c = 14, 7, 11
print(f"The median of {a}, {b}, and {c} is {medain(a, b, c)}")

######## 2 #############

## count word of given sentence
def countwordsofsentence(salam):
    words = sentence.split()
    return len(words)


sentence = "muhammad umer fakih this side and I study in karachi university"
print(f"The number of words in the sentence is: {countwordsofsentence(sentence)}")


####### 6 ##########

def longestsequence(numbers):
  numberset = set(numbers) ##converts input list to set
  longestlength = 0 ##it stores length of longest seq found
  
  for num in numberset:##this iterate over each number in set numberset
      
    if num - 1 not in numberset:##checks if cur numb in start of seq
      currentlength = 1 ##it initialize two variable & store current value
      
      currentnumber = num
      while currentnumber + 1 in numberset:#(1)
          
        currentnumber += 1 #(2)
        
        currentlength += 1 #(3)this loop continue as curr num +1 in set
        
      if currentlength > longestlength:
        longestlength = currentlength ##if cur value is bigger then longest length fount it will update new value
  
  # Return the longestsequence
  return longestsequence     ##longest of length milgai hai
numbers = [100, 4, 200, 5, 7, 6]
print("The longest sequence length is:",longestsequence(numbers))



