words = list(input("Enter the sequence of words : ").split())
words.sort(key=lambda x:x[0].lower())
print("Sorted Words :",*words)