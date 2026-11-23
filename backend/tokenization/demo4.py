word = input("Enter a word: ") or "python"
print("Word = ",word)
print("Length = ",len(word))

characters = list(word)
print("Characters in the given word:",characters)

pairs = list(zip(characters,characters[1:]))

print("Adjacent Pair:",pairs)
