
# # # Simple lopp using range 
# # for i in range(1,6):
# #     print(i)

# # """
# # For loop in list
# # """
# # fruits = ["apple", "banana", "cherry"]
# # for fruit in fruits:
# #     print(fruit)

# # n = len(fruits)

# # for i in range(0,n):
# #     print(i)

# # my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}

# # for key, value in my_dict.items():
# #     print(key, value)

# sample_dict = {'apple':1, 'banana':2, 'cherry':3}

# for key, value in sample_dict.items():
# #     print(key,value)
# #     if(sample_dict['banana']==2):
# #         sample_dict['banana']=3

# # del sample_dict['banana']
# # print(sample_dict)


# # # List example and for loop

# # eg_list = [1,2,3,4,5,6,10,12]
# # n=len(eg_list)
# # print(n)

# # eg_list.insert(2,'car')
# # print(eg_list)
# # i=0

# # while (i < n):
# #     print(i)
# #     i+=1



# a= int(input("Enter the first number"))
# b= int(input("Enter the second number"))
# c= int(input("Enter the third number"))

# if (a>b):
#     if(a>c):
#         print(f"{a} is greater")
#     else:
#         print(f"{c} is greater")
# elif (b>a):
#     if(b>c):
#         print(f"{b} is greater")
#     else:
#         print(f"{c} is greater")


# Password 




# def password_checker (password):
#     condition = False
#     while (condition == False):
#         if len(password) < 8:
#             print("Password must be at least 8 characters long.")
#             password = input("Set your password")
#         elif not any(char.isupper() for char in password):
#             print("Password must contain at least one uppercase letter.")
#             password = input("Set your password")
#         elif not any(char.islower() for char in password):
#             print("Password must contain at least one lowercase letter.")
#             password = input("Set your password")
#         elif not any(char.isdigit() for char in password):
#             print("Password must contain at least one digit.")
#             password = input("Set your password")
#         else:
#             condition = True
#             print("Password meets all requirements.")
            
# password = input("Set your password")
# password_checker(password)



# prompt the user for the number of rows and columns
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))

# create the rug using nested loops
# for i in range(num_rows):
#     print (i)
#     for j in range(num_cols):
#         print("#", end="")
#     print(num_rows) 




for i in range(num_rows):
    print("row cols", num_rows)
    for j in range(num_cols):
        print("num cols", num_cols)
        
    






        
    







