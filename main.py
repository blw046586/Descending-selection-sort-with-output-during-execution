# Read input list from the user
numbers = list(map(int, input().split()))

# Selection sort in descending order
for i in range(len(numbers) - 1):
    max_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[max_index]:
            max_index = j
    numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
    print(numbers)
