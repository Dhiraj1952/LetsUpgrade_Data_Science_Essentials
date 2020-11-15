import numpy as np

#Question1:

a=np.arange(2,51,3)
print(a)

#Question 2:
U1=input("Enter the 5 numbers separted by comma for user 1: ")
U2=input("Enter the 5 numbers separted by comma for user 2: ")
D1=U1.split(",")
D2=U2.split(",")
Num=np.array([[D1],[D2]]) #This will concatenate the two array we can also user #Con=np.concatenate((Num1,Num2))
Sort=np.sort(Num)
print(Num) #Print the concatenatitaion
print(Sort) #This will sort the array

#Question 3

Dim=np.array([1,2,3])
print(Dim.ndim)
print(Dim.size)

#Question 4:
arr_1d=np.array([1,2,3,4,5,6])
arr_2d=np.reshape(arr_1d,(-1,3)) #Cconversion from 1d to 2D
arr_2d=arr_1d[:,np.newaxis]
print(arr_2d.ndim) #Conversion from 1d to 2D with help of newaxis
a = np.arange(6).reshape(2, 3)
print(np.expand_dims(a, 0)) #conversion from 1d to 2d with the help of expand _dims
print(a.ndim)
print(arr_2d.ndim)

#Question 5
a = np.array([[1], [2], [3]])
b = np.array([[2], [3], [4]])
print(np.vstack((a,b)))
c= np.array((1,2,3))
d = np.array((2,3,4))
print(np.hstack((c,d)))

#Question 6

Ucount=np.array([2,3,2,3,4,5,4])
print(np.unique(Ucount,return_counts=True))

