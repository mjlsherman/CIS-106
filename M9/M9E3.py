def change_case(text):
    if text == text.upper():
        new_text = text.lower()
    else:
        new_text = text.upper()

    return new_text


original = input("Enter a string: ")

new_string = change_case(original)

print("Original String:", original)
print("New String:", new_string)
