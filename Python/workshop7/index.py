# """
# Part -1
# """
# # 1 Create a program in Python that opens a file named 'datafile.txt' for reading and assigns identifier input_file to the file object created. 

# # input_file = open("datafile.txt", "r")
# # print(input_file.read())
# # input_file.close()


# # 2
# # try:
# #     output_file = open("datafile2.txt","w")
# #     output_file.write("Hello There How you doing!")

# # except  FileNotFoundError:
# #     print("The file does not exist.")

# # finally:
# #     output_file.close()

# # 3
# # empty_str=""  
# # output_file=open("datafile2.txt","w")
# # input_file = open("datafile.txt","r")

# # line=input_file.readline()
# # while line != empty_str:
# #     output_file.write(line+"\n")

# # 4

# # input_file_opened=False
# # while not input_file_opened:
# #     try:
# #         file_name=input("Enter file name: ")
# #         input_file=open(file_name,"r")
# #         input_file_opened=True
# #     except:
# #         print("File not found")

# # Part 2
# # 1
# def reduce_spaces(line):
#     return ' '.join(line.split())
# line = 'This line has   extra    space characters  '
# print(reduce_spaces(line)) 

# 2 
# def extract_temp(line):
#     temp_str = ''
#     for char in line:
#         if char.isdigit():
#             temp_str += char
#         elif temp_str:
#             break
#     if temp_str:
#         return int(temp_str)
#     else:
#         return None
# line = 'The temperature is 25 degrees Celsius.'
# temp = extract_temp(line)
# if temp:
#     print('The temperature is:', temp) # Output: 'The temperature is: 25'
# else:
#     print('No temperature found.')

# 3
# def check_quotes(line):
#     stack = []
#     for char in line:
#         if char in ['"', "'"]:
#             if not stack or stack[-1] != char:
#                 stack.append(char)
#             else:
#                 stack.pop()
#     return len(stack) == 0
# line = "She said, 'I'm not sure if he'll come.'"
# if check_quotes(line):
#     print('All quotes are matched.')
# else:
#     print('There are unmatched quotes.')


# 4
# def count_letters(line):
#     freq = {}
#     for char in line.lower():
#         if char.isalpha():
#             freq[char] = freq.get(char, 0) + 1
#     return list(freq.items())
# line = 'This is a line'
# letter_freq = count_letters(line)
# print(letter_freq)

# 5
# def interleave_chars(line1, line2):
#     result = ''
#     for char1, char2 in zip(line1, line2):
#         result += char1 + char2
#     return result
# line1 = 'Hello'
# line2 = 'Goodbye'
# interleaved = interleave_chars(line1, line2)
# print(interleaved)

# 6

# line = 'This is a test line.\n'
# count = 0
# for char in line:
#     if char != ' ' and char != '\n':
#         count += 1
# print(count)

# 7. For variable month which contains the full name of any given month, give an expression to display just the first three letters of the month. 

# month = 'September'
# short_month = month[:3]
# print(short_month)





# 8. Give an expression that displays True if the letter ‘r’ appears in a given month name stored in variable month, otherwise displays False.


# month = 'September'
# has_r = 'r' in month
# print(has_r)

# 9 Give an expression for determining how many times the letter ‘r’ appears in a given month name stored in variable month. 
# month = 'September'
# r_count = month.count('r')
# print(r_count)

# 10
# first_name = "Sajan"
# last_name = "Mainali"
# formatted_name = "{}, {}".format(last_name, first_name)
# print(formatted_name)

# 11. Give an instruction that determines if a given social security number represented as a string and stored in variable ss_num, contains any non- digits. 

# ss_num = "123-45-6789"
# has_non_digits = not ss_num.isdigit()
# print(has_non_digits)

# 12. Give an instruction that determines the index of the ‘@’ character in an email address stored in variable email_addr. 
# email_addr = "john.doe@example.com"
# at_index = email_addr.index('@')
# print(at_index)

# 13. For a variable named date containing a date in the form 12/14/2012, give an expression that replaces all slashes characters with dashes.


# date = '12/14/2012'
# new_date = date.replace('/', '-')
# print(new_date)

# 14. For a variable named err_mesg that contains error messages in the form ** error message **, give an expression that produces a string containing the error message without the leading and trailing asterisks and blank characters. 

# err_mesg = '** Error message! **'
# msg = err_mesg.strip('* ').strip()
# print(msg)

# 
# Part 3 

# 1. Write a program that opens and reads a text file and displays how many lines of text are in the file. 
# Open the file for reading
# with open('datafile.txt', 'r') as file:

#     # Read the file and split the contents by line
#     contents = file.read().splitlines()

#     # Count the number of lines in the file
#     num_lines = len(contents)

#     # Display the number of lines in the file
#     print(f'The file contains {num_lines} lines of text.')

# 2. Write a program that reads a text file named original_text, and writes every other line, starting with the first line, to a new file named new_text.

# Open the original file for reading and the new file for writing
# with open('original_text.txt', 'r') as orig_file, open('new_text.txt', 'w') as new_file:

#     # Read the lines of the original file
#     lines = orig_file.readlines()

#     # Write every other line to the new file
#     for i in range(0, len(lines), 2):
#         new_file.write(lines[i])

# 3. Write a program that reads a text file named original_text, and counts how many time the letter 'e' occurs (the most frequently occurring letter in English), and displays how many occurrences there are. 

# filename = "original_text.txt"

# with open(filename, "r") as file:
#     count = 0
#     for line in file:
#         count += line.count("e")

# print("The file", filename, "contains", count, "occurrences of the letter 'e'.")

# 4.  Write a program that reads a text file containing numerical expressions on
# each line and print them out along with the results. For example, for the numerical expression 4 + 2 in your file, your program should output: 4 + 2 = 6. 


with open('original_text.txt', 'r') as file:
    for line in file:
        # remove leading/trailing whitespaces
        expression = line.strip()
        # evaluate expression and print result
        result = eval(expression)
        print(f"{expression} = {result}")









# Lab report 
# Aim: To generate a Global Exception and handle it using the try-except block.

# Objective:
# - Generate a Global Exception by forcing an error.
# - Handle the error using the try-except block.


# Aim: To generate and handle different types of errors in Python.

# Objective:
# - Generate a Zero Division Error by dividing a number by zero.
# - Generate a Value Error by passing an inappropriate value to the int() function.
# - Generate a Global Exception by forcing an error.
# - Handle all errors using the try-except block.


# try:
#     # Zero Division Error
#     result = 10 / 0
    
#     # Value Error
#     num = int("abc")
    
#     # Force an error to generate a Global Exception
#     a = 10 + "abc"
    
# except ZeroDivisionError as e:
#     print("Zero Division Error:", e)
    
# # except ValueError as e:
# #     print("Value Error:", e)
    
# # except Exception as e:
# #     print("Global Exception:", e)


# # Aim: To generate a Global Exception and handle it using the try-except block.

# # Objective:
# # - Generate a Global Exception by forcing an error.
# # - Handle the error using the try-except block.

# # try:
# #     # a = 10 / 0
# #     num = int("abc")
# # except Exception as e:
# #     print("Error:", e)

# # def divide(x, y):
# #     if y == 0:
# #         raise ValueError("Cannot divide by zero.")
# #     return x / y
# # divide(10,0)

# import os

# # Function to read a file
# def read_file(file_path):
#     try:
#         with open(file_path, 'r') as f:
#             contents = f.read()
#             print(contents)
#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found")
#     except PermissionError:
#         print(f"Error: Permission denied for '{file_path}'")
#     except EOFError:
#         print(f"Error: End of file reached while reading '{file_path}'")

# # Testing the function with various file paths
# read_file('nonexistent_file.txt')  # FileNotFoundError
# read_file('/etc/passwd')  # PermissionError (assuming running on a non-Linux machine)
# read_file('sample.txt')  # EOFError (if the file is not properly formatted)




        




