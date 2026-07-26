from argon2 import PasswordHasher
from FileManagement import FileManager
import os

class MasterPassword:
      def __init__(self):
            self.ph = PasswordHasher()
            self.file = FileManager()


      def verify(self, input: str, hash: str) -> bool:
            """Check if input matches hash."""
            try:
                  self.ph.verify(hash, input)
                  return True
            except:
                  return False


      def create_hash(self, input: str) -> str:
            """Make hash of input."""

            # Hash the input
            hashed = self.ph.hash(input)

            self.store_hash(hashed)
            return hashed
      

      def store_hash(self, input: str) -> None:
            """Save hash to file."""
            
            # Create Path
            path = os.path.join(self.file.path(), "hashed_master.bin")

            # Store The Hash
            if not os.path.exists(path):
                  with open(path, "wb") as file:
                        file.write(input)
