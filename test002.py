# n = int(input("Enter the Value of your Own :"))
#
# for i in range(n):
#     print(" "*(n-i-1)+(chr(65+i)+" ")*(i+1))
# for i in range(n-1):
#     print(" "*(i+1)+(chr(63+n-i)+" ")*(n-i-1))
#

# for i in range(n):
#     print(" "*(n-i-1),end=" ")
#     for j in range(i+1):
#         print(chr(65+j), end=" ")
#     print()
# for i in range(n):
#     print(" "*i,end=" ")
#     for j in range(n-i):
#         print(chr(65+j), end=" ")
#     print()


# s= 'one two three four five six'

# l1 = s.split()
# # print(l1)
# i = 0
# l2 =[]
#
# while i<len(l1):
#     if i%2 ==0:
#         l2.append(l1[i])
#     else:
#         l2.append(l1[i][::-1])
#     i = i+1
#
# print(l2)
#
# output = " ".join(l2)
# print(output)


# mylist = s.split()
# mylist1 = []
#
# mylist1=mylist[-1::-1]
# rever = " ".join(mylist1)
# print(rever)


# string should take from User and reverse:

# def reves(str):
#     rev_str = ""
#     for i in str:
#         rev_str = i+rev_str
#     print("Reversied String :", rev_str)
#
#
# str = input("Enter the string as you wish :")
# reves(str)
#
# string = input("enter the alphanumaric value :")
#
# alphabitic = []
# digits = []
#
# for charater in string:
#     if charater.isalpha():
#         alphabitic.append(charater)
#     else:
#         digits.append(charater)
#
# finaloutput = "".join(sorted(alphabitic)+sorted(digits))
#
# print(finaloutputt)

#
# string = input("Enter the string which you wish and see the result of every secound word:")
#
# initallist = string.split()
# # print(len(initallist)) ans = 6
# i = 0

# secoundlist = []
#
# while i<len(initallist):
#     if i%2 == 0:
#         secoundlist.append(initallist[i])
#     else:
#         secoundlist.append(initallist[i][::-1])
#     i = i+1
#
# finaloutput = " ".join(secoundlist)
# print(finaloutput)
#
# string1 = input("enter the value :")
#
# len_str1 = []
#
# for char in string1:
#     if char not in len_str1:
#         len_str1.append(char)
# print(len_str1)
# for char in sorted(len_str1):
#     print("{} occuress {} times ".format(char, string1.count(char)))
#

#
#
# n = int(input("Enter the value :"))
#
#
# for i in range(n):
#     # print(" "*(n-i-1)+(chr(65+i)+" ")*(i+1), end=" ")
#     print((chr(65 + i) + " ") * (i + 1), end=" ")
#     print()
# for i in range(n-1):
#     # print(" "*(i+1)+(chr(63+n-i)+" ")*(n-i-1), end=" ")
#     print((chr(63 + n - i) + " ") * (n - i - 1), end=" ")
#     print()










