def get_integer_list():#first function for getting input from user
    try:
        # Asking the user for input
        num_values = int(input("How many values would you like to enter? "))

        # Initializing
        values = []

        # Loop for the getting values
        for i in range(num_values):
            while True:
                try:
                    # Ask for an input
                    value = int(input(f"Enter integer {i + 1}: "))
                    values.append(value)
                    break  
                except ValueError:
                    print("Invalid input! Please enter an integer.")

        return values

    except ValueError:
        print("Please enter a valid number of values.")


def compute_stats(numbers):#second function for computing sum, average, minimum
    if not numbers:
        return "List is empty."

    # Compute sum, average, minimum
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    minimum_value = min(numbers)
    
    # Compute cumulative sum
    cumulative_sum = []
    current_sum = 0
    for num in numbers:
        current_sum += num
        cumulative_sum.append(current_sum)

    # Return all computed values as a tuple
    return average, minimum_value, total_sum, cumulative_sum


# Using both functions
integer_list = get_integer_list()
print("You entered the following integers:", integer_list)

# Call compute_stats to compute average, minimum, sum, and cumulative sum
if integer_list:  # Make sure the list is not empty
    avg, min_val, total_sum, cum_sum = compute_stats(integer_list)
    print(f"Average: {avg}")
    print(f"Minimum: {min_val}")
    print(f"Total Sum: {total_sum}")
    print(f"Cumulative Sum: {cum_sum}")
