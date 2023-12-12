'''INPUT FUNCTION'''
'''THIS FUNCTION ALLOWS TO TAKE INPUT FROM THE USER AS A STRING'''

'''NOTE - IT IS IMPORTANT TO KNOW THAT THE OUTPUT OF THE INPUT IS ALWAYS A STRING 
EVEN IF YOU ENTER A NUMBER IT WILL READ IT AS A STRING AND RETURN THE VALUE'''


a = input("Enter Your Name : ")
print(type(a))
print("Your Name Is : ", a)

#TYPECASTING

b = input("enter your age : ")
print(type(b))
                   #TYPECATING WILL ONLY WORKS IF BOTH THE INPUT AND THE OUTPUT IS GOING TO BE OF SAME LITERALS
                   #if you input a string and typecast it to integer, you will get error
b = int(b)
print(type(b))

print("your birth year as of 2022 is : ", 2022 - b)