#Project Lovelace, Problem 17
#Caesar cipher

#A famous method of encrypting a message is the Caesar cipher. It involves using a shifted alphabet instead of the regular alphabet. For example, a shift of 13 will involve changing A to N, B to O, C to P, and so on.

import time

def break_caesar_cipher(ciphertext, known_word):
    """Using an encrypted phase and a known word, this function will return the translated message"""
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ''
    for key in range(len(alphabet)):
        for symbol in ciphertext:
            if symbol in alphabet:
                num = alphabet.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(alphabet)
                translated = translated + alphabet[num]
            else:
                translated = translated + symbol
        if known_word in translated.lower():
            return translated.lower()
        else:
            translated = ""

code = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
word = "fox"

start = time.time()
print(break_caesar_cipher(code, word))
print(time.time() - start)
#0.0009987354278564453 secs