# A Set is a collection of unique elements unlike lists or tuples 
#Sets are unordered or immutable and dont allow for duplicates
#You can or remove elements 
#Used to perform a union or intersection
"""
my_set = {1,2,3,4,5}

print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

# Sets supports various operations that allow you to manipulate and compare a collection of elements 
# Union - Combines 2 Sets and removes the duplicate value
# Intersection - Finds the Common Elements in 2 Sets
# Difference finds the elements found 1 set and not the other 
"""

set1 = {1,2,3}
set2 = {3,4,5}

#union combines 2 sets and removes the duplicate value
union_set = set1.union(set2)
print(union_set)

#intersection find the common element in 2 sets
inter_set =set1.intersection(set2)
print(inter_set)

#difference find the elements found 1 set and not the other
diff_set =set1.difference(set2)
print(diff_set)

#sets are useful when you need to work with collections of a unique elements and perform operations like finding intersections, 
# differences or unions between sets
# uses for sets is to remove duplicate data from  list or collection, checking membership and efficiency