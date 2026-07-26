from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes 
from LoggingConfig import Log
from argon2 import PasswordHasher
from hashlib import sha256

class Encryption:
      def __init__(self) -> None:
            self.log = Log("Encryption")

      
      def Generate_key(self, input: str) -> bytes:
            """Make encryption key."""

            # Use Argon2 to derive a secure 256-bit key
            ph = PasswordHasher(
                  time_cost=2,
                  memory_cost=102400,
                  parallelism=8,
                  hash_len=32,
                  salt_len=16
            )
            salt = get_random_bytes(16)  # Generate a random salt
            key = ph.hash(input + salt.hex())  # Derive the key
            return sha256(key.encode('utf-8')).digest()  # Ensure 256-bit output


      def Encrypt(self, data: str, master: str) -> bytes:
            """Encrypt data."""
            aesCipher = AES.new(self.Generate_key(master), AES.MODE_GCM)
            ciphertext, authTag = aesCipher.encrypt_and_digest(data)
            return (ciphertext, aesCipher.nonce, authTag)

      
      def Decrypt(self, nonce: bytes, tag: bytes, data: bytes, master: str) -> str:
            """Decrypt data."""
            

      def clear_memory(self) -> None:
            """Clear sensitive data."""
            pass