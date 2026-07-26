from argon2 import PasswordHasher
import pandas as pd
import datetime, json
from cryptography.fernet import Fernet

class PasswordManager:
      def __init__(self):
            pass


      def get_master_password(self):
            

      
      def hash_this(self, input_parameter):
            ph = PasswordHasher()
            # this hash the password
            hashed_password = ph.hash(input_parameter)

            return hashed_password
      
