from functools import reduce

words = ['Hello', ' ', 'Python', '!']

result = reduce(lambda x, y: x + y, words)

print(result)
