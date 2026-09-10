def caesar_cipher(text, shift):
      shifted = ""
      for char in text:
          if 'a' <= char <= 'z':
              new_pos = ord(char) - ord('a')
              new_pos = (new_pos + shift) % 26
              shifted = shifted + chr(new_pos + ord('a'))

          elif 'A' <= char <= 'Z':
              new_pos = ord(char) - ord('A')
              new_pos = (new_pos + shift) % 26
              shifted = shifted + chr(new_pos + ord('A'))
              
          else:
              shifted = shifted + char
      return shifted


def caesar_decipher(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if 'a' <= char <= 'z':
            new_pos = ord(char) - ord('a') 
            new_pos = (new_pos - shift) % 26
            decrypted += chr(new_pos + ord('a'))

        elif 'A' <= char <= 'Z':
            new_pos = ord(char) - ord('A') 
            new_pos = (new_pos - shift) % 26
            decrypted += chr(new_pos + ord('A'))

        else:
            decrypted += char

    return decrypted

def letter_frequency(text):
    counts = {}
    for i in range(26):
        counts[chr(ord('a') + i)] = 0

    for char in  text.lower():
        if 'a' <= char <= 'z':
            counts[char] += 1

    return counts

def main():
    print("Welcome to the Caesar Cipher Program!")
    print("-----------------------------------------")

    message = input("type the message: ")
    shift = int(input("type the shift value: "))

    cipher_text = caesar_cipher(message, shift)
    deciphered_text = caesar_decipher(cipher_text, shift)
    frequency = letter_frequency(message)

    print("\nResults")
    print("Original Message: ", message)
    print("Encrypted Message: ", cipher_text)
    print("Decrypted Message: ", deciphered_text)
    print("Letter Frequency: ", frequency)

if __name__ == "__main__":
      main()
