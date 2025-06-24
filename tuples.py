# Tuples are Ordered
# Represent a list of items that cannot be modified 
# Unordered 

my_tuples = (1,2,3,4,5)
print (my_tuples)

#Can access items in tuple by using Indexing similar to lists 
print(my_tuples[0])
print(my_tuples[1])
print(my_tuples[2])
print(my_tuples[-1]) # Gives us the last value in our Data Collection 

#Concatenating tuples 
tuple1 = (1,2,3)
tuple2 = (4,5,6)

conc_tuple = (tuple1 + tuple2)
print (conc_tuple)

#Doing repetition with Tuples 
conc_tuple = tuple1 + tuple2
rep_tuple =  tuple1 * 3
print(rep_tuple)


#Tuples are suitable for situations where you store a collection fo elements that should not be changed or halt your program execution 
# Tuples store fixed collection of data, co-oridnates, database codes, rgb codes 