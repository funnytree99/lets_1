from collections import Counter

def letter_frequency(text):
    text = text.lower()
    letters = [char for char in text if char.isalpha()]
    return Counter(letters)

text = input("Введите текст: ")
freq = letter_frequency(text)
print("Частота букв:")
for letter, count in sorted(freq.items()):
    print(f"'{letter}': {count}")