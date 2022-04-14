
# ID: 20CS067
# Name: Tanvi Radia
# Python program to sum all the items in a dictionary

# Function to print sum
def returnSum(dict1):
    list = []
    for i in dict1:
        list.append(dict1[i])
    final = sum(list)
    return final


# Driver Function
dict1 = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}
print("Sum:", returnSum(dict1))
