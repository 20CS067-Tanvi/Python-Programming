
# ID: 20CS067
# Name: Tanvi Radia
# Python script to check whether a given key already exists in a dictionary
dict1 = {
    1: "Roti",
    2: "Sandwitch",
    3: "Pizza",
    4: "Pani Puri"
}

# Function to check whether key is present or not
def key_present(n):
    if n in dict1:
        print("Yes", n, "is present in our Dictionary")
    else:
        print("No", n, "is not present in our Dictionary")


key_present(3)  # Function call
key_present(5)
