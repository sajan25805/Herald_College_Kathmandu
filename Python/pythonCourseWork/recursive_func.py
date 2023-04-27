
# def fact(n):
#     if n>0:
#         return n*fact(n-1)
#     else:
#         return 1
# print(fact(5))



# print(lists([2,3,4])) 

# def sum(n):
#     if len(n)==0:
#         return 0
#     else:
#         print()
#         return n[0] * sum(n[1:]) 
# print (sum([1, 3, 4, 2, 5]))
 

def reverse(n):
    if len(n)==0:
        return []
    else:
        print(n[:-1])
        return [n[-1]]+reverse(n[:-1])
reverse([1, 3, 4, 2, 5])

        













    