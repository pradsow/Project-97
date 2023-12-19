# print("Happy Birthday Girl!!")

# a , b , c = 100,34,67

# # ----------------------------------------------------------------------------------------------------

# # by default , input() takes the input in string

# # name = input("Enter Your Name : ")

# # print(type(name))

# # str , int , float , bool (boolean) , dictionary , list

# # age = int(input("Enter Your Age : "))

# # print(type(age))

# # ----------------------------------------------------------------------------------------------------

# print("---------------------------------------------")

# # function defination statement --> you need to recieve the arguments in this statement.
# def greeting(name):
#     print("Hello " , name)

# # function call statement --> we can pass arguments while calling the function.
# greeting("Veda Samhita")

# #button greeting()

# # ----------------------------------------------------------------------------------------------------

# # f = (c * 9/5) + 32

# print("---------------------------------------------")

# def fareheit(t):
#     far = (t * (9/5)) + 32
#     print(far)


# temp = float(input("What is the temperature? (In Celcius)  "))
# fareheit(temp)

# # ----------------------------------------------------------------------------------------------------

# print("---------------------------------------------")
# def voting(age):
#     if age < 18:
#         print("Sory! you can't vote!!")
#     elif age == 18 :
#         print("Get your docs ready!!")
#     else :
#         print("you can vote!!")


# #age = int(input("What is your age? (Don't lie!) : "))
# voting(age)

# ----------------------------------------------------------------------------------------------------

# if cond1 or cond2 :  --> if you want any of the condition to be true

# if cond1 and cond2 :  --> if you want both of the condition to be true

print("---------------------------------------------")

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("This year is a leap year!!!")
    else :
        print("Sorry! this year is not a leap year!!!")

year = int(input("Please enter a year :  "))
leap_year(year)











