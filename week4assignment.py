def modify_file():
    # Ask user for input and output filenames
    input_file = input("Enter the filename to read: ")
    output_file = input("Enter the filename to save modified content: ")

    try:
        # Try to open and read file
        with open(input_file, "r") as file:
            content = file.read()
            print("\nOriginal content read successfully!\n")

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Write modified content to new filefile
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"Modified content written to '{output_file}'")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You don’t have permission to read '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
modify_file()
