# 🚆 Simple Train Details Parser

filepath = r"chapter 11\trains.txt"

train_dict = {}  # To store all train details

# ----------- READING FILE LINE BY LINE -----------
with open(filepath, "r") as file:
    for line in file:
        line = line.strip()  # Remove spaces and newlines
        
        # Skip empty lines
        if not line:
            continue
        
        # Split the line into parts wherever there's an underscore
        parts = line.split("_")
        
        # Skip invalid lines (we need at least 4 parts: number + name + source + destination)
        if len(parts) < 4:
            continue
        
        # First part is always the train number
        train_number = parts[0]
        
        # Last two parts are source and destination
        source = parts[-2]
        destination = parts[-1]
        
        # Everything in between is the train name
        train_name = "_".join(parts[1:-2])
        
        # Store details in the dictionary
        train_dict[train_number] = {
            "name": train_name,
            "source": source,
            "destination": destination
        }

# ----------- PRINTING TRAIN DETAILS -----------
print("\n🚉 TRAIN DETAILS 🚉")
for train_no, details in train_dict.items():
    print(f"{train_no} → {details['name']} ({details['source']} → {details['destination']})")
