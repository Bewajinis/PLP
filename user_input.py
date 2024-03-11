# name = input('what is your name?  ')
# age = input('how old are you?  ')
# location = input('which location are you?  ')

# you = (f'Hello {name}, you are {age} years old and live in {location}. ')

# print(you)

#Condition Statement
# Grading in A School.

# marks = int(input("Enter your score:" ))

# if marks >= 80 and marks <= 100:
#     print("Your Grade is A")

# elif marks >= 70 and marks <= 79:
#     print("Your Grade is B")

# elif marks >= 60 and marks <= 69:
#     print("Your Grade is C")

# elif marks >= 50 and marks <= 59:
#     print("Your Grade is D")

# elif marks >= 40 and marks <= 49:
#     print("Your Grade is Failed")

# else:
#     print("this is out of range")


#this is a while loop 

# x = 10
# while x < 10:
#     print(x)
#     x +=1


# #sum of num 1+2+3+4......+n
# n = int(input("enter number: "))
# sum = 0
# x = 1 #this is my counter

# while x <= n:
#     sum = sum + x
#     if sum == 20:
#         break
#     x += 1
#     print(sum)

# print (f"My final answer is: ", sum )

# # This is FOR loop
# num = [[1, 2],[ 4, 5, 6]]

# for  i in num:
#     for item in i:
#     # # i +=1
#     # if i < 1:
#     #     continue
#         print(item)

# def large_power(base, exponent):
#     if base ** exponent > 5000:
#         return True
#     else:
#         return False
    
# print(large_power(1, 4))


# def divisible_by_ten(num):
#     if num % 10 == 0:
#         return True
#     else: 
#         return False
    
# print(divisible_by_ten(40))
    
def calculate_discount(price, discounted_percent):
    if discounted_percent >= 0.20:
        final_price = price - (price * discounted_percent) 
        return final_price
    else:
        return price

original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage (as a decimal): "))
final_price = calculate_discount(original_price, discount_percent)


print(f"The final price is: ", final_price)