def is_second_largest_exists(num_array):
    new_array = set(num_array)
    new_array.remove(max(new_array))
    if len(new_array) == 0:
        return -1
    return max(new_array)


try:
    nums_array = list(map(int, input("Enter only Integers separated by space : ").split()))
    print(is_second_largest_exists(nums_array))
except ValueError:
    print("Invalid input. Enter Only Integers")
