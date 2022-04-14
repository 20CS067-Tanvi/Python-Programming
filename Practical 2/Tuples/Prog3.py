
# ID: 20CS067
# Name: Tanvi Radia
# Python program to add an item in a tuple

# Add item into a tuple
tuple_before = ("Apple", "Mango", "Banana")
print("Tuple before Adding an item: ", tuple_before)
tuple_to_list = list(tuple_before)
tuple_to_list.append("Orange")
tuple_after = tuple(tuple_to_list)
print("Tuple after adding an item: ", tuple_after)

# Add tuple to a tuple
tuple_before = ("Apple", "Mango", "Banana")
print("Tuple before Adding an item: ", tuple_before)
add_item = ("Orange",)
tuple_after = tuple_before+add_item
print("Tuple after adding an item: ", tuple_after)


