def add_info(name, address):
    with open("users.txt", "a") as f:  # Use 'a' to append
        f.write(name + address,"\n")  # Add newline for proper formatting

def read_info():
    with open("users.txt", "r") as f:  # Use 'r' to read
        for line in f:
            print(line.strip())

# Example usage
add_info("julen", "baneshwor")
add_info("Jayson", "baneshwor")
read_info()