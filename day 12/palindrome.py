def is_palindrome(string):
    string = string.replace(" ", "").lower()
    if string == string[::-1]:
        return f"'{string}' is a palindrome."
    else:
        return f"'{string}' is not a palindrome."
print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("Python"))
print(is_palindrome("A man a plan a canal panama"))
