# import pickle
# d={}
# f=open("student.dat","wb")
# a="y"
# while a=="y" or a=="Y":
#     a=int(input("enter number of records to be inserted:"))
#     for i in range(a):
#         r=int(input("Enter roll no:"))
#         n=input("Enter name:")
#         m=float(input("Enter marks:"))
#         d["roll no"]=r
#         d["name"]=n
#         d["marks"]=m
#         pickle.dump(d,f)
#     a=input("want to enter more records! if yes then enter y :")
# f.close()
# import pickle
# f=open("student.dat","rb")
# try:
#     while True:
#         s=pickle.load(f)
#         print(s)
# except EOFError:
#     print("file not found")
#     f.close()
import pickle 
f=open("student.dat","rb")
while True:
    s=pickle.load(f)
    if s['marks']<60:
        print(s['name'])
f.close()
