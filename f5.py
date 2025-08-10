def count_words(text):
    words = text.split()
    return len(words)

text = input("Введите текст: ")
word_count = count_words(text)
print(f"Количество слов: {word_count}")

if word_count > 0:
    unique_words = len(set(text.lower().split()))
    print(f"Количество уникальных слов: {unique_words}")
else:
    print("Текст пуст!")