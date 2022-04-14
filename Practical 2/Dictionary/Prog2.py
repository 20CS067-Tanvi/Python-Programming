
# ID: 20CS067
# Name: Tanvi Radia
# Python script to merge two Python dictionaries
dict1 = {
    1: 'a',
    2: 'b',
}
dict2 = {
    3: 'c',
    4: 'd',
}
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)


def merge(dict1, dict2):
    return dict1.update(dict2)


merge(dict1, dict2)
print("Merged Dictionaries:", dict1)


