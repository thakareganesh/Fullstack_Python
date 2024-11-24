try:
    fname = input("Enter file name with extension: ")
    # Use 'with' to manage file opening and closing
    with open(fname, 'r') as file:
        data = file.read()
        if data.strip():  # Check if the file is not empty
            print(data)
        else:
            print("The file is empty.")
except FileNotFoundError:
    print(f"Sorry..! The file '{fname}' was not found.")
except PermissionError:
    print(f"Permission denied to access the file '{fname}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")