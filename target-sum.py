def find_digits_that_sum(number_str, target_sum):
    total_sum = 0
    used_digits = []

    for i in number_str:
        if i.isdigit():
            digit = int(i)
            if total_sum + digit <= target_sum:
                total_sum += digit
                used_digits.append(digit)

            if total_sum == target_sum:
                print('The digits used:', used_digits)
                print('The total sum:', total_sum)
                return  # Exit the function once found

    # If the loop completes without finding the sum
    if total_sum != target_sum:
        print("No combination of digits adds up to the target sum.")


# Example usage
number_str = input("Enter digits: ")  # Example: 12345
target_sum = int(input("Enter target sum: "))  # Example: 4

find_digits_that_sum(number_str, target_sum)
