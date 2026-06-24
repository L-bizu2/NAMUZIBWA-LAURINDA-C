# Exe2: Using Lambda with sorted(), arrange using length of the words


words = ['Cherry', 'Banana', 'Date', 'Apple', 'Mango', 'DragonFruit']

sorted_words = sorted(words, key=lambda x: len(x))


print("Original List:")

print(words)

print("-" * 40)



print("Sorted by Word Length (Shortest to Longest):")

print(sorted_words)