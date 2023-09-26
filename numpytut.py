import numpy 
#1. print even array
#a = numpy.arange(0,101,2)
#print(a)

#2.test whether elemrnt is less than 100
#a=numpy.array([1,100,101,70])
#print(a<100)


#3. Determine size of array and compare with list
arr = numpy.array([1,2,4,6,8,9])
print("Size of Array:",arr.size)
print("Memory Size of array",arr.size*arr.itemsize, "bytes")


#4. NxN identity matrix
n = int(input("Enter a number: "))
arr = numpy.eye(n, dtype=int)
print(arr)


#5. Remove all number from array greate than or equal to given number
n=int(input())
arr = numpy.array([11,22,36,4,63,82,92,41,59])
narr=numpy.delete(arr,numpy.where(arr>=n))
print(narr)

