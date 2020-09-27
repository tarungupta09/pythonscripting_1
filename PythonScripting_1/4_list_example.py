# ATTRIBUTES OF A LIST
#
# 1. It is Indexed
# 2. It is mutable
# 3. It supports duplicate data





# students names, attending the session today

# datatype: list

# index ===>  0         1            2         3       4          5
attendees = ['Biswa', 'Ranjeetha', 'Siddiq', 'Gupta', 'Vishal', 'Areen']
print(attendees)

# print out a specific indexed name
print(attendees[4])


# reverse the entire list
attendees.reverse()
print(attendees)

# add a new attendee
attendees.append('Biswa')
print(attendees)


# delete an existing attendee
attendees.remove('Areen')
print(attendees)


# sorting the attendees (optionally, reversed sort)
attendees.sort(reverse=True)
print(attendees)