letters = input("Give data: ")

# Prompt the user for the number of columns and the order of addition
num_columns = int(input("Enter the number of columns: "))
order = input("Enter the order of addition (e.g., '1234' for sequential or '2413' for a custom order): ")

# Create column lists based on the user's input
column_lists = [[] for _ in range(num_columns)]

i = 0
for letter in letters:
    col_index = int(order[i % len(order)]) - 1  # Subtract 1 to convert to a 0-based index
    column_lists[col_index].append(letter)
    i += 1

finalarr = []
for column in column_lists:
    finalarr.extend(column)

final = "".join(finalarr)
print(final)