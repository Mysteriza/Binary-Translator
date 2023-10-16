# Function to convert text to binary representation
def text_to_binary(text):
    # Using list comprehension to convert each character to 8-bit binary representation
    binary_result = " ".join(format(ord(char), "08b") for char in text)
    return binary_result


# Function to convert binary to text representation
def binary_to_text(binary):
    # Splitting binary values into a list and converting back to characters
    binary_values = binary.split()
    text_result = "".join(chr(int(bin_val, 2)) for bin_val in binary_values)
    return text_result


# Main function to drive the program
def main():
    # Displaying options for the user
    print("Choose an option:\n1. Text to Binary\n2. Binary to Text")
    # Asking for user input
    choice = input("Enter your choice (1/2): ")

    # If the user chooses option 1
    if choice == "1":
        text_input = input("Enter text: ")  # Asking for text input
        binary_output = text_to_binary(text_input)  # Calling text_to_binary function
        print("Result: ", binary_output)  # Displaying the binary output

    # If the user chooses option 2
    elif choice == "2":
        binary_input = input("Enter binary: ")  # Asking for binary input
        text_output = binary_to_text(binary_input)  # Calling binary_to_text function
        print("Result: ", text_output)  # Displaying the text output

    # If the user enters an invalid choice
    else:
        print("Invalid choice. Please select 1 or 2.")


# Ensuring the program starts from the main function
if __name__ == "__main__":
    main()
