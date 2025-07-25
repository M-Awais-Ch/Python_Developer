# # for i in range(0, len(a)):
# #     if a[i]==9:
# #         a.pop(i)
# #         break
# #     print(f"phase {i}:::::::::",a)
# a=[5,2,6,2,7,1,2,9,4]
# i=0
# for j in range(1,len(a)):
#     if a[i]==a[j]:
#      print(a[i])
#      i+=1
#
# #p1: Remove l character from string
# data = "hello world"
#
#
# #p2: Reverse words in a given String
# data = "hello world"
#
# # p3: Python Program to Check if a String is Palindrome or Not
# s = "malayalam"
#
# #p4: Interchange first and last elements in a list
# my_list = [1, 2, 3, 4, 5]
#
# #p4: Python Program to Swap Two Elements in a List
# a = [10, 20, 30, 40, 50]
#
#
# #p5: Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.
# Input: s = "geEksforGEeks"
# Output: "geEksforG"
# #Explanation: After removing duplicate characters such as E, e, k, s, we have string as "geEksforG".
#
#
#
# #p6: Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not. Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.
# #Example 1
# #Input: s1 = "geeks" s2 = "kseeg"
# #Output: true
# #Explanation: Both the string have same characters with same frequency. So, they are anagrams.
#
# #Example 2
# # Input: s1 = "allergy", s2 = "allergyy"
# # Output: false
# # Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams.
#
# print(a)
# # print(a)
# # print(a[5])
# # print(a[1:6])
# # print(a[-5:])
# # #b=[(x**3,x*2,x) for x in a]
# # print(a.append(19))
# # # a[3]=8
# # print(a)
# # a.pop(2)
# # print(a)
#
# # print(a.pop(3))
# # print(a)
# # a.pop([1])
# # print(a)
#
#
a=[3,32,4,3,22,3,4,2,4,3]
def check(b):
    return b>5
print(list(filter(check,a)))