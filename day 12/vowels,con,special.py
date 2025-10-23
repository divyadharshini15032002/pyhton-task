def count_characters(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    special_count = 0

    for char in string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
        elif not char.isspace():
             special_count += 1
                                        
print("Given string:", 'string')
print("Number of Vowels:", 'vowel_count')
print("Number of Consonants: ", 'consonant_count')
print("Number of Special characters:", 'special_count') 

