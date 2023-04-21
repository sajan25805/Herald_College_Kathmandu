# f=open('./sajan.txt','r')

# print(f.read())

# f.close()

# f= open('sajan.html','r')
# line= f.readline()
# print(line)
# while line!="":
#     print(line)
#     line=f.readline()
# checker=""
# with open("data.txt", "r") as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         for w in word:
#            value=len(w)
#            if len(checker)<value:
#                checker=w

# print(checker)


# # open the file for reading
# file = open('filename.txt', 'r')

# # read the contents of the file
# # contents = file.read()

# # close the file
# file.close()

# # print the contents of the file
# # print(contents)




# # Open a file for reading
# file = open('filename.txt', 'r')
# contents = file.read()
# print("Contents of the file:")
# print(contents)
# file.close()

# # Open a file for writing
# file = open('filename.txt', 'w')
# new_contents = input("Enter new contents: ")
# file.write(new_contents)
# print("File has been updated with new contents.")
# file.close()

# # Open a file for appending
# file = open('filename.txt', 'a')
# new_contents = input("Enter additional contents to append: ")
# file.write('\n' + new_contents)
# print("File has been updated with additional contents.")
# file.close()


# # Open a file for reading
# file = open('filename.txt', 'r')
# contents = file.read()
# print("Contents of the file:")
# print(contents)
# file.close()

# # Open a file for writing
# file = open('filename.txt', 'w')
# new_contents = input("Enter new contents: ")
# file.write(new_contents)
# print("File has been updated with new contents.")
# file.close()

# # Open a file for appending
# file = open('filename.txt', 'a')
# new_contents = input("Enter additional contents to append: ")
# file.write('\n' + new_contents)
# print("File has been updated with additional contents.")
# file.close()

"""
Lab WEEK 7
"""
#2.	Write a program to count the number of upper-case alphabets present in a text file “PYTHON.TXT”.


# final_data=""

# count=0

# with open('sajan.txt','r') as file:
#    temp = list(file.read())
#    for data in temp:
#     checker = data.isupper()


#     if(checker == True):
#         count = count+1
#         final_data += data


# print(count)

# with open("munu.txt",'w') as file:
#     file.write(final_data)

# print(final_data)


# 4 Write a Python program to write a list content to a file. 
# (Sample list (color =['Red','Green', 'White', 'Black', 'Pink', 'Yellow'])   


# color =['Red','Green', 'White', 'Black', 'Pink', 'Yellow']

# with open("color.txt","w") as f:
#    f.write("List of colors:")
#    for c in color:
#       f.write("\n"+c)


# 5 
"""
Write a Python program that reads a text file named "data.txt" and finds the longest word in the file. 
The program should use a loop to read each line of the file, 
split each line into words using the split () method, and then iterate over each word to find the longest one. Once the loop has finished,
the program should print the longest and shortest and equal length words found in the file.

"""


   
# # Open the file in read mode


   


#  




# # with open("formdata.txt", "a") as f:
#     name = input("Enter your name: ")
#     age = input("Enter your age: ")
#     qualification = input("Enter your qualification: ")
#     description = input("Enter a brief description about yourself: ")
#     hobby = input("Enter your hobby: ")
#     interest = input("Enter your interests: ")
    
#     f.write(f"Name: {name}\n")
#     f.write(f"Age: {age}\n")
#     f.write(f"Qualification: {qualification}\n")
#     f.write(f"Description: {description}\n")
#     f.write(f"Hobby: {hobby}\n")
#     f.write(f"Interest: {interest}\n")
#     f.write("-" * 30 + "\n")

# Print success message
# print("Form data saved successfully!")





