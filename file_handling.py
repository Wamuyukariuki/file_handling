def create_file():
  """Creates a new text file named "my_file.txt" and writes content to it."""
  try:
    with open("my_file.txt", "w") as file:
      file.write("This is the first line of text.\n")
      file.write("Here's a number: 42\n")
      file.write("Another line with some text.\n")
    print("Successfully created and wrote to my_file.txt")
  except Exception as e:
    print(f"Error creating file: {e}")

def read_file():
  """Reads the contents of 'my_file.txt' and displays them on the console."""
  try:
    with open("my_file.txt", "r") as file:
      contents = file.read()
      print("Contents of my_file.txt:")
      print(contents)
  except FileNotFoundError:
    print("Error: File 'my_file.txt' not found.")
  except Exception as e:
    print(f"An error occurred while reading the file: {e}")

def append_to_file():
  """Opens 'my_file.txt' in append mode and writes additional lines."""
  try:
    with open("my_file.txt", "a") as file:
      file.write("Appending some more text.\n")
      file.write("Here's another line.\n")
      file.write("This is the final appended line.\n")
    print("Successfully appended content to my_file.txt")
  except PermissionError:
    print("Error: Insufficient permission to append to the file.")
  except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Call the functions to perform operations
create_file()
read_file()
append_to_file()
read_file()
