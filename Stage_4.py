# Stage 4: Reading from a File (Multiple Sets of Inputs)
print("\nStage 4: Reading from a File (Multiple Sets of Inputs)")

try:
    with open("output.txt", "r") as file:
        for line in file:
            pill_data = line.strip().split(" ")
            if len(pill_data) != 3:
                print(f"Invalid entry in output.txt: {line.strip()}")
                continue

            pill_name, pill_time, dosage = pill_data

            # Simulate notification
            print(f"Reminder: Take your pill '{pill_name}' at {pill_time} - Dosage: {dosage}")

except FileNotFoundError:
    print("Error: output.txt file not found.")
except ValueError:
    print("Error: Invalid data in output.txt file.")