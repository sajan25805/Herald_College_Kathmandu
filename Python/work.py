

"""
8.Write a python program to print this address as it is.
Herald College Kathmandu,
Naxal, PO:44600
Kathmandu, Nepal
"""



# print( " Herald College Kathmandu,"
#      "  \n Naxal , PO: 44600 "
#       " \n Kathmandu,Nepal ")



n = int(input("Enter a number: "))
i=1
count=0

if n==0 or n==1:
     print("It is neither prime nor composite")

else:
    while i<=n:
        if(n%i==0):
             count+=1
    i=i+1
    if count <=2:
     print("It is a prime")
    else:
     print("It is a composite")
























