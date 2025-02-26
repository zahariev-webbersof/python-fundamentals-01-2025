numbers = list(map(int, input().split()))
average_sum = sum(numbers) / len(numbers)
greater_numbers_than_average_sum = [num for num in numbers if num > average_sum]

if greater_numbers_than_average_sum:
    top_five_nums = sorted(greater_numbers_than_average_sum, reverse=True)[:5]
    print(' '.join(map(str, top_five_nums)))
else:
    print('No')

