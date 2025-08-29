#Read a File and Handle Errors
file_name = "sample.txt"

try:
    with open(file_name, "r") as file:
        contents = file.read()
        print("Reading file content: ")
        print(contents.strip())

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")

