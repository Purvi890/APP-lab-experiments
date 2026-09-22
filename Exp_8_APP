# Open the input file and read all lines
with open("input.txt", "r") as file:
    lines = file.readlines()

# Count total number of lines
line_count = len(lines)

# Extract the first two lines
first_two_lines = lines[:2]

# Display the number of lines
print("Total number of lines:", line_count)

# Display the first two lines
print("First two lines:")
for line in first_two_lines:
    print(line, end="")

# Write the first two lines to the output file
with open("output.txt", "w") as file:
    file.writelines(first_two_lines)

print("\nFirst two lines written to output.txt")
