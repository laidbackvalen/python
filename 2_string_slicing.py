greeting = "Good Morning, "
name = "Valen!"

#CONCATENATING 2 STRINGS
print(greeting + name)  #this will add 2 strings

#or

c = greeting + name
print(c)

print("\n")
print("\n")

name = 'valen' #str length = 5, indexs will be 0-4

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# name[3] = "valen"   #does not support item assignment  #no chanes will be done to a string like this

# print(name[3])

'''-------------------------------------------------------------------------------------------------------------'''


'''STRING SLICING - this is the process use to slice a string'''

 #"v" is on index value 0, 
 # "a" on 1, 
 # "l" on 2, 
 # "e" on index 3, 
 # "n" on 4
 
 # anything[index_start : index_end]  
                
print(name[0:2])  #string slice will start from 0 index to 1 index value
                  #this will print "va"
                  # [0:2] means 0 to 1 , here [0:2] 0 is including and and 2 is excluding
                  #index 2 is not included
                  
print(name[2:4]) #this will slice name "valen" and print the value of index 2 to 3 
                 #which is "le"
                 # [2:4] means 2 to 3 ,  here [2:4] 2 is including and and 4 is excluding
                 
                  
print(name[4:5]) #this will print index 4 value as there is no index 4 whic will be "n"
                 # [4:5] means 4  , here [4:5] 4 is including and and 5 is excluding
                 
                 
                 

'''you can also do this'''
print(name[:4]) #this will start printing string from minimun index which is 0 to 3
                #prints "vale"  #same as name[0:4]
                
print(name[0:])  #this start printing index value 0 and last index value # "valen" 
                 #same as name[0:4] , name[0:length]
                 
print(name[2:])  #starts with index 2 value which is "l" and ends with last index value
                 #same as name[2:4]
                 
                 
'''--------------------------------------------------------------------------------------------------------'''                 
                
                
'''NEGATIVE INDEX'''
'''negative indexing means the indexing starts from the end of the string'''

#the last element is at index -1, the second last index is at -2 and so on. 
# where -1 denotes "n" , -2 denotes "e" , -3 denotes "l" , -4 denotes "a" and -5 denotes "v"

 
print(name[-5 : ]) #this will start printing index value of -5 to -1

#print(name[-2:-5]) #invalid as you cannot print string in from opposite side as -5 index holds value of "n" and -2 hold value of "a"
                   #it will not print "nela"

print(name[-4 : -1])  #this will print "ale" as -1 index value is not included

c = name[-4 : -2]
print(c)



'''-------------------------------------------------------------------------------------------------------------------------------------------'''

'''SLICING WITH SKIP VALUE'''
#VALEN

print(name[1:4:2])  
                    #name[1:4] is meant to print "ale" but
                    #the last ":2" is to skip every 2nd index value start from index 1 to 4
                    #prints "a" as 1st included index, skips "l" as is the 2nd value in index starting from "a"
                    #prints "e" as its 1st after skip and skip "n" as it's 2nd value after 1st skip
                    #so finally it will prints "ae" as a result
                    
                    
print(name[0:5:2])  #with only name[0:5] "valen" will be printed but
                    #using ":2" will skip every 2nd index value while printing index 0 to 5
                    #will print first index "v" skip 2nd index "a", 
                    #print 1st index after skipping "a" which is "l" than skip "e" as it's 2nd and prints "n" as it's 1st index
                    
print(name[2:4:2])

name = "valen rajubhai patel" #overriding the variable  #means changing the value of the variable 
print(name[0::2])
print(name[:5:1])
print(name[:5:3])


