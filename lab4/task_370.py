text = input("Please enter your text: ")
letter = input("Please enter your letter: ")

#Пошук першої появи letter (пошук зліва)
first = text.find(letter)

#Пошук останньої появи letter (пошук справа)
last = text.rfind(letter)

left_part = text[:first]
right_part = text[last + 1:]

print(left_part + right_part)
