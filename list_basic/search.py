n = int(input())
word = input()

strings = [input() for _ in range(n)]
filtered_strings = [current_string for current_string in strings if word in current_string]

print(strings)
print(filtered_strings)