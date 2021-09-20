def cipher(direction, shift, text):
    text_split = list(text)

    text_split = [ord(i) for i in text_split]

    text_shift = [str(i + (direction * shift)) for i in text_split]

    return str.join(',', text_shift)


def decipher(direction, shift, text):
    text_split = str.split(text, ',')

    text_shift = [chr(int(i) - (direction * shift)) for i in text_split]

    return str.join('', text_shift)


if __name__ == '__main__':
    string = "The encryption step performed by a Caesar cipher is often" \
             " incorporated as part of more complex schemes, such as the Vigenère cipher" \
             ", and still has modern application in the ROT13 system. As with all single-alphabet" \
             " substitution ciphers, the Caesar cipher is easily broken and in modern practice offers " \
             "essentially no communication security."

    encrypted_string = cipher(-1, 4, string)
    print(encrypted_string)
    print(decipher(-1, 4, encrypted_string))