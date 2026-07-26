from FileManagement import FileManager
from tkinter import filedialog
import sqlite3
import datetime
import pandas as pd
from LoggingConfig import Log
import os
import shutil


class Database:
      # Count logins that have been deleted/added
      data_added = 0
      data_deleted = 0

      def __init__(self):
            """
            Initializes the Database class, establishes a connection to the database,
            and ensures the required table exists. If the database file does not exist,
            it creates a new one and informs the user.
            """
            self.file = FileManager()

            # Check if the database file exists; if not, notify the user
            if not os.path.exists(self.file.database_pointer()):
                  # Placeholder for a popup function to notify the user
                  # db_creation_popup() 
                  pass
            
            # Establish a connection to the database
            self.conn = sqlite3.connect(self.file.database_pointer())
            self.cursor = self.conn.cursor()
            
            # Configure logging
            self.log = Log("Database")

            # Create the required table if it does not exist
            self.create_table()

      def create_table(self) -> None:
            """
            Creates the `kmps_db` table in the database if it does not already exist.
            """
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS kmps_db (
                                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    Username TEXT NOT NULL,
                                    Password TEXT NOT NULL,
                                    Note TEXT,
                                    Service TEXT NOT NULL,
                                    Date TEXT NOT NULL,
                                    TAG BLOB NOT NULL,
                                    NONCE BLOB NOT NULL
                              )""")
             
            # Load the table into a pandas DataFrame for further operations
            self.dataframe = pd.read_sql("SELECT * FROM kmps_db", self.conn)

            # Placeholder for a popup function to notify the user
            # db_creation_popup()

      def commit(self) -> None:
            """
            Commits changes to the database and closes the connection.
            Logs the number of added and deleted records.
            """
            try:
                  self.conn.commit()
                  self.conn.close()
                  self.log.info(f"Committed database changes [ +{self.data_added} | -{self.data_deleted} ]")

            except sqlite3.Error:
                  self.log.error("SQLite3 Error occurred during commit.", exc_info=True)
                  # Placeholder for error handling
                  # error_message()

            except:
                  self.log.error("An unexpected error occurred during commit.", exc_info=True)
                  # Placeholder for error handling
                  # error_message()

            finally:
                  # Reset counters for added and deleted records
                  self.data_added = 0
                  self.data_deleted = 0

      def add_login(self, Username: str, Password: str, Note: str, Service: str, Nonce: bytes, Tag: bytes) -> None:
            """
            Adds a new login record to the database.

            Args:
                  Username (str): The username for the login.
                  Password (str): The password for the login.
                  Note (str): Additional notes for the login.
                  Service (str): The service associated with the login.
                  Nonce (bytes): The nonce used for encryption.
                  Tag (bytes): The tag used for encryption.
            """
            try:
                  self.cursor.execute("INSERT INTO kmps_db (Username, Password, Note, Service, Date, Nonce, Tag) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                                      (Username, Password, Note, Service, datetime.date.today(), Nonce, Tag))
                  self.data_added += 1
                  self.log.info("Added a new login record.")

            except sqlite3.Error:
                  self.log.error("SQLite3 Error occurred while adding a login.", exc_info=True)
                  # Placeholder for error handling
                  # error_message()

            except:
                  self.log.error("An unexpected error occurred while adding a login.", exc_info=True)
                  # Placeholder for error handling
                  # error_message()

      def remove_login(self, index: str) -> None:
            """
            Removes a login record from the database by its ID.

            Args:
                  index (str): The ID of the login record to be removed.
            """
            try:
                  self.cursor.execute("DELETE FROM kmps_db WHERE ID = ?", (index,))
                  self.data_deleted += 1
                  self.log.info("Deleted a login record.")
            
            except sqlite3.Error:
                  self.log.error("SQLite3 Error occurred while removing a login.", exc_info=True)
                  # Placeholder for error handling
                  # error_message()

            except:
                  self.log.error("An unexpected error occurred while removing a login.", exc_info=True)

      def view_database(self):
            """
            Displays the contents of the database for debugging purposes.
            This method is intended for development and may be removed in production.
            """
            query = "SELECT * FROM kmps_db"
            data = self.cursor.execute(query)
            print(self.cursor.fetchall())
            print()

            print(self.dataframe)

            print("Columns:")
            for num, column in enumerate(data.description):
                  print(f"{num}) {column[0]}")

      def return_connection(self):
            """
            Returns the active database connection.

            Returns:
                  sqlite3.Connection: The active database connection.
            """
            return self.conn

      def return_table(self) -> tuple:
            """
            Retrieves all records from the `kmps_db` table.

            Returns:
                  tuple: A tuple containing all records from the table.
            """
            self.cursor.execute("SELECT * FROM kmps_db")
            return self.cursor.fetchall()

      def update(self, column: str, value: any) -> None:
            """
            Updates a specific column in the database with a new value.

            Args:
                  column (str): The column to be updated.
                  value (any): The new value to set for the column.
            """
            self.cursor.execute(f"UPDATE kmps_db SET {column} = ?", (value,))

      def create_backup(self) -> None:
            """
            Creates a backup of the current database in the backup folder.
            """
            self.log.info("Creating a backup of the database.")
            
            backup_path = os.path.join(self.file.path_of_backup_folder(), f"KMPS!db {datetime.date.today()}")
            shutil.copyfile(self.file.database_pointer(), backup_path)

            self.log.info("Backup created successfully.")

      def switch_database(self) -> None:
            """
            Switches to a different database file selected by the user.
            Ensures the selected file is of the correct type (.db).
            """
            path = filedialog.askopenfile(initialdir=self.file.path_of_backup_folder())
            
            # Verify if the user selected the correct file type
            if not path.endswith(".db"):
                  # Notify the user that the selected file is not of the correct type
                  # Placeholder for error handling
                  # error_message()
                  pass
            else:
                  # Update the database pointer to the selected file
                  self.file.database_pointer(path)
