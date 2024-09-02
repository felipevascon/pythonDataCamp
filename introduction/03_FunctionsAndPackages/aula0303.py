############### STRING METHODS ####################


# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted (full, reverse=True)

# Print out full_sorted
print (full)
print (full_sorted)


############### LISTS METHODS ####################
#01

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))

#02

# Create list newAreas
newAreas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
newAreas.append(24.5)
newAreas.append(15.45)

# Print out newAreas
print(newAreas)

# Reverse the orders of the elements in areas
newAreas.reverse()

# Print out areas
print(newAreas)