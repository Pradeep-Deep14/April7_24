#Count of Unique Letters of Each Elements

Fruits = ['Apple', 'Banana', 'Mango']
unique_letters_dict = {}

for fruit in Fruits:
    unique_letters = set(fruit)
    unique_letters_count = len(unique_letters)
    unique_letters_dict[fruit] = unique_letters_count

print("Count of unique letters for each element:")
print(unique_letters_dict)

#Easy Method

fruits = ['apple', 'banana', 'orange', 'kiwi', 'strawberry']

for fruit in fruits:
    unique_letters = set(fruit)
    print(f"{fruit}: {len(unique_letters)} unique letters")
