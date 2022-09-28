# -*- coding: utf-8 -*-
"""DAA pertemuan 5 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gi5xavf6CL3yUg6dmm9zz6O_Ez12qTIo

Algoritma Divide And Conquer

#Hitung Inversi
"""

def countInversion(arr):
    result=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                result+=1
    return result

arr=[21, 70, 36, 14, 25]

result=countInversion(arr)
print(result)

"""implementasi algoritma

hitung inversi dengan divide and conquer
"""

def countInversiondua(abc):
  icount=0
  if len(abc) <=1:
    return icount

  mid=len(abc)//2
  left=abc[:mid]
  right=abc[mid:]
  icount+=countInversiondua(left)
  icount+=countInversiondua(right)
  i=j=k=0

#Print(left)
#Print(right)
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      abc[k]= left[j]
      i+=1
    else:
      #print(left[i],right[j])
      abc[k]= right[j]
      j+=1
      icount+= (mid-i)
    k+=1
  while i<len(left):
    abc[k]=left[i]
    i+=1
    k+=1
  while j<len(right):
    abc[k]=right[j]
    j+=1
    k+=1
  return icount

abc=[1, 20, 6, 4, 5]

result = countInversiondua(abc)
print(result)

"""maximum subarray sum"""

# tanpa divide and conquer

def maxSubSum(arr):
    max_so_far=0
    max_ending_here=0
    for i in range(len(arr)):
        max_ending_here+=arr[i]
        if max_ending_here>max_so_far:
            max_so_far=max_ending_here
        if max_ending_here<0:
            max_ending_here=0
    return max_so_far

arr=[ -2, -5, 6, -2, -3, 1, 5, -6]
result=maxSubSum(arr)
print(result)

"""maximum subarray sum"""

#menggunakan divide and conquer

def maxCrossingSum(arr,low,mid,high):
    result=0; leftSum=float('-infinity')
    for i in range(mid,low-1,-1):
        result+=arr[i]
        if result>leftSum:
            leftSum=result
    result=0; rightSum=float('-infinity')
    for i in range(mid+1,high+1):
        result+=arr[i]
        if result>rightSum:
            rightSum=result
    return leftSum+rightSum


def maxSum(arr,low,high):
    if low==high:
        return arr[low]
    mid=(low+high)//2
    return max(maxSum(arr,low,mid),maxSum(arr,mid+1,high),maxCrossingSum(arr,low,mid,high))

arr=[ -2, -5, 6, -2, -3, 1, 5, -6]
result=maxSum(arr,0,len(arr)-1)
print(result)

"""longest common prefix"""

from re import S
from os.path import commonprefix
#dengan divide and conquer

def commonPrefix(str1,str2):
    n1=len(str1);n2=len(str2)
    i,j=0,0
    s=""
    while i<n1 and j<n2:
        if str1[i]==str2[j]:
           s+=str1[i]
           i+=1
           j+=1
        else:
             break
    return s

def longestCommonPrefix(arr,low,high):
    if low==high:
        return arr[low]
    mid=(low+high)//2
    result1=longestCommonPrefix(arr,low,mid)
    result2=longestCommonPrefix(arr,mid+1,high)
    result=commonPrefix(result1,result2)
    return result

arr=['geeksforgeeks', 'geeks', 'geek', 'geezer']

result=longestCommonPrefix(arr,0,len(arr)-1)

print(result)

arr=["apple", "ape", "april"]
result=longestCommonPrefix(arr,0,len(arr)-1)
print(result)

"""median dua urut array urut sama ukuran"""

#median dari dua array dengan divide and conquer

def medianOfArray(arr1,arr2,n):
  m1=-1 #first number
  m2=-1 #second number
  count=0
  i=j=0
  while count<n+1:
    count+=1
    if i==n: # i==5 index error if arr1[i]<arr2[j] is checked
        m1=m2
        m2=arr2[0]
        break
    if j==n:
        m1=m2
        m2=arr1[0]
        break
    if arr1[i]<arr2[j]:
       m1=m2
       m2=arr1[i]
       i+=1
    else:
       m1=m2
       m2=arr2[j]
       j+=1
  return (m1+m2)//2

arr1=[1, 12, 15, 26, 38]
arr2=[2, 13, 17, 30, 45]

print(medianOfArray(arr1,arr2,len(arr1)))

"""median dua array urut berbeda ukuran"""

#Flloor in sorted array

def floorSorted(arr,low,high,x):
  #print(low,high)
  if low>high:
      return -1

  if arr[low]>x:
  #print("inside")
     return -1

  if arr[high]<=x:
      return arr[high]

  mid=(low+high)//2

  if arr[mid]==x:
      return arr[mid]

  if mid>0 and x>=arr[mid-1] and arr[mid]>x:
      return arr[mid-1]

  if mid<high and x<arr[mid+1] and x>=arr[mid]:
      return arr[mid]
  
  if x>arr [mid]:
      return floorSorted(arr,mid+1,high,x)
  else:
       return floorSorted(arr,low,mid-1,x)

arr=[1,2,8,10,12,14,19]

x=5

print(floorSorted(arr,0,len(arr)-1,x))

"""nilai terdekat"""

#mencari nilai terdekat dengan metode divide dan conquer

def closestNumber(arr,low,high,x):
    if low>high:
        return -1
    if arr[high]<=x:
        return arr[high]
    if arr[low]>=x:
        return arr[low]
    mid=(low+high)//2
    if arr[mid]==x:
        return arr[mid]
    abs_mid=abs(arr[mid]-x)
    if mid>0:
        abs_left=abs(arr[mid-1]-x)
        if abs_left<abs_mid:
            return closestNumber(arr,low,mid-1,x)
    if mid<high:
        abs_right=abs(arr[mid+1]-x)
        if abs_right<abs_mid:
            return closestNumber(arr,mid+1,high,x)
    #print('after')
    return arr[mid]

arr=[2, 5, 6, 7, 8, 8, 9]

x=9

print(closestNumber(arr,0,len(arr)-1,x))

"""fixed point"""

#mencari fixed point dengan metode divide dan conquer

def fixedPoint(arr,low,high):
    if low>high:
        return -1
    if arr[high]==high:
        return arr[high]
    if arr[low]==low:
        return arr[low]
    mid=(low+high)//2
    if arr[mid]==mid:
        return arr[mid]
    if mid>arr[mid]:
        return fixedPoint(arr,mid+1,high)
    else:
        return fixedPoint(arr,low,mid-1)

arr=[9, 1, 4, 5, 2]

print(fixedPoint(arr,0,len(arr)-1))