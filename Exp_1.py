text = "CRYPTOGRAPHY"
text = text.upper()

for k in range(1, 26):
    encrypted = ""

    for ch in text:
        if ch.isalpha():
            encrypted += chr((ord(ch) - 65 + k) % 26 + 65)
        else:
            encrypted += ch

    print("Shift", k, ":", encrypted)
