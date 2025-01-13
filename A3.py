#Q1
def count_vowels(text):
    vowels = "aeiou"
    
    count = sum(1 for char in text.lower() if char in vowels)
    return count

text = "Hello World"

print(count_vowels(text))


#Q2

def find_max(numbers):
   
    if not numbers:
        return None
    
    max_value = numbers[0]
    
    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value

numbers = [3, 5, 2, 8, 1]

print(find_max(numbers))

