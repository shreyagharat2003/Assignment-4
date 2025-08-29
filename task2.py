#Write and Append Data to a File
f1 = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(f1 + "\n")

f2 = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(f2 + "\n")

print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
