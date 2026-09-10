import unittest
from p5_Bradford_Doyle import caesar_cipher, caesar_decipher, letter_frequency


class TestCipherFunctions(unittest.TestCase):

    def test_encrypt_lowercase(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")

    def test_encrypt_uppercase(self):
        self.assertEqual(caesar_cipher("XYZ", 2), "ZAB")

    def test_encrypt_with_spaces_and_punctuation(self):
        self.assertEqual(caesar_cipher("Hello, World! 123", 3), "Khoor, Zruog! 123")

    def test_decrypt_basic(self):
        self.assertEqual(caesar_decipher("def", 3), "abc")

    def test_decrypt_with_mixed_characters(self):
        self.assertEqual(caesar_decipher("Khoor, Zruog! 123", 3), "Hello, World! 123")

    def test_letter_frequency_basic(self):
        expected = {
            'a': 2, 'b': 2, 'c': 2, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
            'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
            'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
            'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }
        self.assertEqual(letter_frequency("abcabc"), expected)

    def test_letter_frequency_ignores_case(self):
        expected = {
            'a': 2, 'b': 2, 'c': 2, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
            'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
            'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
            'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }
        self.assertEqual(letter_frequency("AaBbCc"), expected)

    def test_letter_frequency_ignores_nonletters(self):
        expected = {
            'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 1, 'f': 0, 'g': 0,
            'h': 1, 'i': 0, 'j': 0, 'k': 0, 'l': 2, 'm': 0, 'n': 0,
            'o': 1, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
            'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }
        self.assertEqual(letter_frequency("Hello!!! 123"), expected)


if __name__ == "__main__":
    unittest.main()