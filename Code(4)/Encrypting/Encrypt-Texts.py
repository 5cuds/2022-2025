from cryptography.fernet import Fernet

# Generate a key (only do this once and save the key securely)
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt a message # b'd'
message = input("Enter Text Tou Tant To Encrypt: ").encode()
encrypted_message = cipher.encrypt(message)

# Decrypt the message
decrypted_message = cipher.decrypt(encrypted_message).decode()

print("Encrypted: ", encrypted_message)
print("Decrypted:", decrypted_message)