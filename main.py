# import random 
# import math 
# def linear_search(arr,target):
#     for x in range(len(arr)):
#         if target == arr[x] :
#             return x 
#     return -1
# numbers = [1,2,3,4,5,6,7,8,9]
# print(linear_search(numbers,10))

# def binary_search(arr,target):
#     left= 0 
#     right = len(arr) -1 
#     while left<=right :
#         mid = (left+right)//2
#         if target == arr[mid]:
#             return mid 
#         elif target < arr[mid]:
#             left = mid +1 
#         else:
#             right = mid -1 
#     return -1
# numbers = [1,2,3,4,5,6,7,8,9]        
# print(len(numbers))
# print(binary_search(numbers,0))

# def first_occurance(arr,target):
#     left = 0
#     right = len(arr) -1 
#     result = -1
#     while left<=right:
#         mid = (left+right)//2
#         if arr[mid] == target :
#             result = mid 
#             right  = mid  - 1
#         elif target < arr[mid] :
#             left = mid + 1
#         else:
#             right  = mid - 1 
#     return result 
# numbers = [1,2,3,4,4,4,4,4,4,4,4,5,5,5,5,6]        
# print(first_occurance(numbers,6))

# def last_occurance(arr,target):
#     left = 0 
#     right = len(arr)-1
#     result = -1
#     while left<=right:
#         mid = (left+right)//2
#         if arr[mid] == target :
#             result = mid 
#             left = mid +1 
#         elif arr[mid] < target :
#             right = mid -1
#         else:
#             left = mid + 1
#     return mid
# numbers = [1,2,3,4,4,4,4,4,4,4,4,5,5,5,5,6]       
# print(last_occurance(numbers,5))

# def two_pointers(list,n):
#     left = 0 
#     right = len(list)-1
#     result = 0 
#     while left<right :
#         total = list[left] + list[right]
#         if total == n :
#             result +=1
#             left +=1
#             right -=1
#         elif total < n:
#             left +=1
#         else:
#             right -=1
#     return result 
# numbers = [1,2,3,4,6,7,8,9]
# print(two_pointers(numbers,10))        

# def two_sum(list,target):
#     left = 0 
#     right = len(list)-1
#     while left<right :
#         total = list[left] + list[right]
#         if total == target :
#             return [left,right] 
#         elif total < target :
#             left +=1
#         else:
#             right -=1
# numbers = [1,2,3,4,6,7,8,9]
# print(two_sum(numbers,10))

# def two_sum(list,x):
#     left = 0 
#     right = len(list) - 1
#     result = []
#     while left<right :
#         total = list[left] + list[right]
#         if total == x :
#             result.append(left)
#             result.append(right)
#             left +=1
#             right -=1
#         elif total <x:
#             left +=1
#         else:
#             right -=1
#     return result 
# numbers = [1,2,3,4,6,7,8,9]        
# print(two_sum(numbers,10))

# def IsPolindrome(x):
#     temp = x 
#     reverse = 0
#     while temp>0:
#         digit = temp%10
#         reverse = reverse*10 +digit 
#         temp//=10
#     return reverse == x 
# print(IsPolindrome(126544566))            

# def IsArmstrong(n):
#     temp = n 
#     result = 0 
#     digits = len(str(n))
#     while temp>0:
#         digit = temp%10
#         result +=digit **digits 
#         temp //=10
#     return result == n 
# print(IsArmstrong(153))    

# def IsPerfect(y):
#     result = 0
#     while y >0:
#         for x in range(1,y):
#             if y%x==0:
#                 result+=x
#         return y==result 
    
# print(IsPerfect(28))            

# def prefix_sum(arr):
#     prefix = [0] * (len(arr)+1)
#     for x in range(len(arr)):
#         prefix[x+1] = prefix[x] + arr[x]
#     return prefix     
# numbers = [1,2,3,4,5,6,7,8,9]
# print(prefix_sum(numbers))

# def L_to_R(arr,L,R):
#     prefix = [0] * (len(arr)+1)
#     for x in range(len(arr)):
#         prefix[x+1] = prefix[x]  + arr[x]
#     return prefix[R+1] - prefix[L]  
# numbers = [1,2,3,4,5,6,7,8,9]  
# print(L_to_R(numbers,3,5))

# class Solution:
#     def checkPerfectNumber(self,num:int) -> bool:
#         if num <=1:
#             return False 
#         total_sum = 1 
#         for i in range(2,int(num**0.2)+1):
#             if num % i== 0 :
#                 total_sum+=i
#                 if i * i!=num:
#                     total_sum += num//i
#         return total_sum==num 
            



# def IsTarget(arr,target):
#     result = -1
#     for x in range(len(arr)):
#         if arr[x] == target :
#             result = x 
#             return result 
#     return result 
# arr = [1,2,3,4,5,6]
# print(IsTarget(arr,5))


# def CountTarget(arr,target):
#     result = 0 
#     for x in range(len(arr)):
#         if arr[x] == target :
#             result +=1
#     return result 
# arr = [1,2,3,4,4,4,4]      
# print(CountTarget(arr,4))


def MinTarget(arr):
    minimum = arr[0] 
    for x in range(len(arr)):
        if arr[x] < minimum:
            minimum = x
    return minimum 
arr = [8, 3, 5, 1, 9, 1, 7].sort()
print(MinTarget(arr))        








    



