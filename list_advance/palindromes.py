words = input().split()
palindrome = input()

palindrome_list = [word for word in words if word == word[::-1]]
number_of_special_palindrome = palindrome_list.count(palindrome)

print(palindrome_list)
print(f'Found palindrome {number_of_special_palindrome} times')