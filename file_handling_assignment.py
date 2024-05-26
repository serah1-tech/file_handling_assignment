def create_file():
    try:
        # Open "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write three lines of text to the file
            file.write("This is line 1\n")
            file.write("Line 2: 42\n")  # Writing a mix of string and number
            file.write("Third line")

        print("File 'my_file.txt' created successfully.")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File creation process completed.\n")


def read_and_display():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            print("Contents of 'my_file.txt':")
            print(file.read())

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File reading process completed.\n")


def append_to_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the file
            file.write("\nAppending line 1\n")
            file.write("Appending line 2: Hello\n")
            file.write("Appending line 3: World\n")

        print("Additional content appended to 'my_file.txt'.")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    finally:
        print("File appending process completed.\n")


if __name__ == "__main__":
    # File Creation
    create_file()

    # File Reading and Display
    read_and_display()

    # File Appending
    append_to_file()
