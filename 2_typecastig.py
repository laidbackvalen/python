''' TYPE FUNCTION IS USED TO FIND THE DATA TYPES OF A GIVEN VARIABLE '''

'''TYPE CASTING IS THE WAY TO CONVERT ONE DATA TYPE TO ANOTHER'''

'''EVEN AFTER TYPE CASTING MAKE SURE BOTH THE VARIABLE BECOMES OF SAME DATA TYPES'''

'''IF YOU TRY TO TYPECAST 19valen9 INTO INTEGER IT WON'T BE POSSIBLE'''


a = "1997"         #the number 1997 is written in double cot so interpreter reads it as a string
print(type(a))     #variable "a" is a string so the return type will be string
                  

a = int(a)         #typecasting of "a" from string to integer #THIS WILL CONVERT "a" AS INTEGER
print(type(a))     #variable "a" will return as a integer here
print(a+25)


#integer to string

b = 14            #"b" is a integer
print(type(b))    #use this function to know the data type
print(b)          #print b before type casting #this will show "b" as a integer

b = str(b)        #typecasting b as a string from integer
print(type(b))    #prints the data type   #this will show "b" as a string
print(b)          #print b after typecasting

#integer to float

c = 2
print(type(c))
print(c)

c = float(c)
print(type(c))
print(c)