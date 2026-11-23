#Word level tokenization
text = input("Enter a text: ") or "I love learning python"
print("Text = ",text)
print("Length = ",len(text))
tokens = text.split()
print("Tokens:",tokens)
print("Number of tokens:",len(tokens))

