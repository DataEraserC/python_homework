def caesar_encrypt(text, shift = 3):
    encypted_text=""
    for char in text:
        if not char.isalpha():
            char = char
        else:
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = (char_code-ord('a')+shift)%26
            char_code += ord('a')
            char = chr(char_code)
            if is_upper:
                char = char.upper()
        encypted_text += char
    return encypted_text





def caesar_decrypt(encrypted_text, shift = 3):
    decrypted_text=""
    for char in encrypted_text:
        if not char.isalpha():
            char = char
        else:
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = (char_code-ord('a')-shift)%26
            char_code += ord('a')
            char = chr(char_code)
            if is_upper:
                char = char.upper()
        decrypted_text += char
    return decrypted_text

text = "Hello, World!"
shift = 3

encrypted_text = caesar_encrypt(text, shift)
print("加密后的文本:", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("解密后的文本:", decrypted_text)
