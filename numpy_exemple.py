import numpy as np

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])
y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])

#We print information about Y
print('Y has dimensions:', x.shape)
print('Y has a total of', x.size, 'elements')
print('Y is an object of type:', type(x))

# We save x into the current directory as
np.save('my_array', x)

# We load the saved array from our current directory into variable y
z = np.load('my_array.npy')
print("z=", z)

#Create np array with zeros
zero_array = np.zeros((3,4), dtype=int)

 #Create np array with ones
one_array = np.ones((3,4), dtype=int)

#Create a np array with constant values
full_array = np.full((4,5), 5, dtype=int)

#create identity matrix
identity_matrix = np.eye(5)

#diagonal matrix
diagonal_matrix = np.diag(10,20,30,40,50)

#array de range to integer (start, stop and incremente)
array_range = np.arange(10)

#array de range to float (start, stop and number of elements)
array_range_flot = np.linspace(1,10,20, endpoint=false)

#convert an array to a matrix (number of elements is important)
range_array_reshape = np.reshape(array_range,(2,5))

# ----------- np array functions can be use as methods --------------#

#create a random array (3x3 matrix with random number betweem zero and one)
random_array = np.random.random((3,3))

#create a random array (3x2 matrix with random number 4 and 15)
random_array = np.random.randint(4,15, (3,3))




# ------------------ delete elements in an array ------------------------#
# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print x
print()
print('Original x = ', x)

# We delete the first and last element of x
x = np.delete(x, [0,4])

# We print x with the first and last element deleted
print()
print('Modified x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We delete the first row of y
w = np.delete(Y, 0, axis=0)

# We delete the first and last column of y
v = np.delete(Y, [0,2], axis=1)

# We print w
print()
print('w = \n', w)

# We print v
print()
print('v = \n', v)


# ------------------- append elements into an array -------------------------#
# We append a new row containing 7,8,9 to y
v = np.append(Y, [[7,8,9]], axis=0)

# We append a new column containing 9 and 10 to y
q = np.append(Y,[[9],[10]], axis=1)

# We insert the integer 3 and 4 between 2 and 5 in x.
x = np.insert(x,2,[3,4])

# We create a rank 1 ndarray
x = np.array([1,2])

# We create a rank 2 ndarray
Y = np.array([[3,4],[5,6]])

# We print x
print()
print('x = ', x)

# We print Y
print()
print('Y = \n', Y)

# We stack x on top of Y
z = np.vstack((x,Y))

# We stack x on the right of Y. We need to reshape x in order to stack it on the right of Y.
w = np.hstack((Y,x.reshape(2,1)))

# We print z
print()
print('z = \n', z)

# We print w
print()
print('w = \n', w)


# ----------- ATENTIO! SLICING DOES NOT CREATE A COPY OF AN ARRAY!!!! --------#
