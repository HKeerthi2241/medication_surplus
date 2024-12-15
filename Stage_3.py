# Stage 3: Reading from a File (Single Set of Input)

print("\nStage 3: Reading from a File (Single Set of Input)")

try:
    # Open and read the input file
    with open("input.txt", "r") as file:
        line = file.readline().strip().split(" ")
        
        # Unpack the contents into variables
        pill_name, pill_time, dosage = line

        # Simulate notification
        print(f"Reminder: Take your pill '{pill_name}' at {pill_time} - Dosage: {dosage}")

except FileNotFoundError:
    print("Error: input.txt file not found.")
except ValueError:
    print("Error: Invalid data in input.txt file.")