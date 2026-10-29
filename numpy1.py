# import numpy as np
# print(np.__version__)                #check the version

# numbers=np.array([10,20,30,40])
# print(numbers)
# print(type(numbers))

# a=np.zeros(5)
# print("zeros : ",a)          #zeros are built in fn to create a array of 0's only. the resulyt is shown a s float


# b=np.ones(5)
# print("ones : ",b)           #ones are built in fn to create a array of 1's only.

# c=np.arange(1,11)
# print("range : ", c)          #arange is used to create a array of numbers from 1-10


# d=np.arange(2,21,2)
# print("range with step : ",d)

# odd=np.arange(1,11,2)
# print("odd numbers : ",odd)


# e=np.linspace(1,10,3)
# print("linspace : ",e)            #used for evently space. takes total and find the mind value and adds from the starting value till the end of the range


# a=np.array([10,20,30,40])
# b=np.array([
#     [10,20,30],
#     [40,50,30]
# ])

# print("1D Array : ",a)
# print("2D array : ",b)


# print("dimension : ",a.ndim)          #dimension give whether array are 1D or 2D
# print("shape : ",a.shape)             #shape gives the number od rows or columns
# print("total elemets : ",a.size)      #size gives the total number of elements in the array

# print("dimension : ",b.ndim)
# print("shape : ",b.shape)
# print("total elemets : ",b.size)

# a=np.array([10,20,30])
# b=np.array([1.5,10.5,20.5])
# c=np.array([True,False,True])

# print(a.dtype)                    #dtype is used to find the data type of the elements inside the array
# print(b.dtype)
# print(c.dtype)

# marks=np.array([75,55,25,66])
# print("first marks : ",marks[0])
# print("third matk : ",marks[2])
# print("last mark : ",marks[-1])

# marks[1]=95
# print("updated marks : ",marks)

#slicing
# numbers=np.array([10,20,30,40,50,60])
# print(numbers[1:4])
# print(numbers[3:])
# print(numbers[::2])
# print(numbers[::-1])

# marks=np.array([
#     [80,85,90],
#     [70,75,80],
#     [90,95,98]
# ])

# print("first row : ",marks[0])
# print("second row, third sub : ", marks[1,2])
# print("first column : ",marks[:,0])
# print(marks[:2,:])


                                            #mathematical and arithmatic operations

# marks=np.array([65,70,80,85,90,95])

# print("total : ",np.sum(marks))
# print("mean : ",round(np.mean(marks),2))
# print("median : ",np.median(marks))
# print("mininum : ",np.min(marks))
# print("maximum : ",np.max(marks))
# print("std : ",round(np.std(marks),2))

                                            #axis=0       column-wise operation
                                            #axis=1       row-wise operations

# marks=np.array([
#     [80,70,90],
#     [60,85,75],
#     [90,95,85]
# ])

# print("student average : ")
# print(np.mean(marks, axis=1))

# print("subject average : ")
# print(np.mean(marks, axis=0))

# print("student total : ")
# print(np.sum(marks, axis=1))


                                #np.random.seed(10)     helps to stabilize the random numbers
                                #rant - float numbers between 0 to 1
                                #randint- random numbers between a range

# np.random.seed(10)

# a=np.random.randint(1,101,size=5)
# b=np.random.rand(5)

# print("random integer : ",a)
# print("random decimal : ",b)

                                          #sorting

# marks=np.array([78,45,92,65,88,54])
# sorted_marks=np.sort(marks)

# print("ascending : ", sorted_marks)
# print("descending : ",np.sort(marks)[::-1])
# print("original : ",marks)


                                       #Arithmetic operations

# a=np.array([10,20,30])
# b=np.array([1,2,3])

# print("addition : ",a+b)
# print("subtraction : ",a-b)
# print("multiplication : ",a*b)
# print("division : ", a/b)
# print("power : ",a**2)


# numbers=np.arange(1,13)

# matrix=numbers.reshape(3,4)
# print(numbers)
# print(matrix)
# print("shape",matrix.shape)

# a=np.array([10,20,30])
# b=np.array([40,50,60])

# print("joined: ",np.concatenate((a,b)))
# print("vertical stack : ",np.vstack((a,b)))      #2-dimensional
# print("horizontal stack : ",np.hstack((a,b)))    #1-dimensional


                         #BOOLEAN INDEXING- FILTER USING CONDITION

# marks=np.array([45,78,32,90,65,28,85])

# passed=marks[marks>=40]
# failed=marks[marks<40]
# high_score=marks[marks>=80]

# print("passed : ",passed)
# print("failed : ",failed)
# print("high score : ",high_score)




