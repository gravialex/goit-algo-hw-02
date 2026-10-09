from collections import deque

def is_palindrome(input_string: str) -> bool:
    # Normalize the string: convert to lowercase and remove all spaces
    normalized_string = "".join(input_string.lower().split())
    
    # Create a deque and add all characters of the string
    char_deque = deque(normalized_string)
    
    # Compare characters from both ends of the deque
    while len(char_deque) > 1:
        # Remove and return a character from the right and left ends
        left_char = char_deque.popleft()
        right_char = char_deque.pop()
        
        if left_char != right_char:
            return False
            
    return True

def main():

    test_strings = [
        "A man a plan a canal Panama",
        "Racecar",
        "Hello",
        "Was it a car or a cat I saw",
        "Python",
        "Oleksii Oleksii"
    ]
    
    print("===++ Palindrome Checker ++===")
    for text in test_strings:
        result = is_palindrome(text)
        print(f"'{text}' -> Palindrome: {result}")

if __name__ == "__main__":
    main()