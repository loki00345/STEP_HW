#1
# def is_palindrome(input_str):
#     # Видалимо пробіли і переведемо рядок в нижній регістр
#     input_str = input_str.replace(" ", "").lower()
    
#     return input_str == input_str[::-1]

# user_input = input("Введіть рядок: ")

# if is_palindrome(user_input):
#     print("Введений рядок - паліндром!")
# else:
#     print("Введений рядок - не паліндром!")


#2
# def change_reserved_words(text, reserved_words):
#     words = text.split()

    
#     for i in range(len(words)):
#         if words[i] in reserved_words:
#             words[i] = words[i].upper()

    
#     changed_text = " ".join(words)
#     return changed_text


# user_text = input("Введіть текст: ")


# reserved_words_input = input("Введіть список зарезервованих слів через кому: ")


# reserved_words = [word.strip() for word in reserved_words_input.split(",")]


# modified_text = change_reserved_words(user_text, reserved_words)


# print("Змінений текст:", modified_text)


#3
def count_sentences(text):
    sentence_terminators = ['.', '!', '?'] 
    sentence_count = 0

    # Проходимо по кожному символу у тексті
    for char in text:
        # Перевіряємо чи поточний символ є кінцем речення
        if char in sentence_terminators:
            sentence_count += 1
        # elif char == '.':
        #     sentence_count +=1

    return sentence_count

user_text = input("Введіть текст: ")


num_sentences = count_sentences(user_text)

print(f"У введеному тексті {num_sentences} речень.")
