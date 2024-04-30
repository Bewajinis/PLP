# Create a new text file named "my_file.txt" in write mode ('w')
try:
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("Line 1: Hello, this is my_file.txt!\n")
        file.write("Line 2: A big Shoutout to all my instructors.\n")
        file.write("Line 3: My password is 12345")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File creation process completed.")

# Read and display the contents of "my_file.txt"
try:
    with open("my_file.txt", "r") as file:
        print("\nContents of my_file.txt:")
        print(file.read())

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File reading process completed.")

# Append three additional lines of text to "my_file.txt"
try:
    with open("my_file.txt", "a") as file:
        file.write("\nLine 4: Appended line 1.\n")
        file.write("Line 5: Appended line 2.\n")
        file.write("Line 6: 67890")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("File appending process completed.")
