try:
    with open("my_file.txt", "w") as file:
        file.write("Hello World!\n")
        file.write("I am 19\n")
        file.write("Come say hi!\n")
      
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of the file after writing:")
        print(contents)

    with open("my_file.txt", "a") as file:
        file.write("Yes, we're doing it!\n")
        file.write("Do hard things\n")
        file.write("Won't stop now!\n")

    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of the file after appending:")
        print(contents)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File operations completed.")
