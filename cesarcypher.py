def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Shift the character by the specified amount
            shifted_char = chr(((ord(char) - ord('A' if is_upper else 'a') + shift) % 26) + ord('A' if is_upper else 'a'))
            
            encrypted_text += shifted_char
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_text += char
    
    return encrypted_text

# Example usage:
text = input("enter text:")
shift = int(input("enter shift value:"))
encrypted_text = caesar_cipher(text, shift)
print("Original text:", text)
print("Encrypted text:", encrypted_text)