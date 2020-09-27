# ATTRIBUTES OF A SET
#
# 1. It is NOT Indexed
# 2. It is Mutable
# 3. It DOES NOT support duplicate data





# students names, attending the session today
# datatype: set

attendees = {'Biswa', 'Ranjeetha', 'Siddiq', 'Gupta', 'Siddiq', 'Areen', 'Ranjeetha', 'Siddiq'}
print(type(attendees))

print(attendees)


# add new entry
attendees.add('Ramesh')
print(attendees)

# adding a duplicate entry shows no errors, but does not add also
attendees.add('Gupta')
print(attendees)

# removal
attendees.remove('Areen')
print(attendees)
