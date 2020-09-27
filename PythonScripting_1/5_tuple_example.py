# ATTRIBUTES OF A TUPLE
#
# 1. It is Indexed
# 2. It is Immutable
# 3. It supports duplicate data





# students names, attending the session today
# datatype: tuple
# index ===>  0         1            2         3       4          5        6           7
attendees = ('Biswa', 'Ranjeetha', 'Siddiq', 'Gupta', 'Siddiq', 'Areen', 'Ranjeetha', 'Siddiq')
print(type(attendees))
print(attendees[4])
print(attendees)

count_of_siddiq = attendees.count('Gupta')
print(count_of_siddiq)

index_of_areen = attendees.index('Areen')
print(index_of_areen)

