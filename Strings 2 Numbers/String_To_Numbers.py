units = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19
}

tens = {
    "twenty": 20, "thirty": 30, "forty": 40,
    "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninety": 90
}

scales = {
    "hundred": 100,
    "thousand": 1_000,
    "lakh": 1_00_000,
    "crore": 1_00_00_000,
    "million": 1_000_000,
    "billion": 1_000_000_000
}

def words_to_number(words):
    current = 0
    total = 0

    for word in words:
        if word in units:
            current += units[word]
        elif word in tens:
            current += tens[word]
        elif word == "hundred":
            current *= 100
        elif word in scales:
            current *= scales[word]
            total += current
            current = 0
        else:
            raise ValueError(f"Unknown number word: {word}")
    
    return total + current


user_input = input("Enter a string of numbers separated by spaces: ")
numbers_str = user_input.lower().strip().split()

try:
    result = words_to_number(numbers_str)
    print("Converted number:", result)
except ValueError as e:
    print("Error:", e)
