input_string = input("Enter a string: ")
vowel_count = 0
vowels = set("aeiouAEIOU")

for char in input_string:
    if char in vowels:
        vowel_count += 1

print(f"Number of vowels in the given string: {vowel_count}")