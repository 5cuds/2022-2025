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
            Init DB, connect, and check table.
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
            Make `kmps_db` table if not exist.
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
            Save changes and close DB.
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
            Add login to DB.
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
            Delete login by ID.
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
            Show DB content (debug only).
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
            Get DB connection.
            """
            return self.conn


      def return_table(self) -> tuple:
            """
            Get all records from DB.
            """
            self.cursor.execute("SELECT * FROM kmps_db")
            return self.cursor.fetchall()


      def search(self, input: str) -> list:
            """
            Search logins in DB.
            """

            # A list to store filtered Dataframes
            store = []

            for column in ["Password"]:
                  filtered_df = self.dataframe[self.dataframe[column].astype(str).str.contains(input, na=False)]
                  store.append([tuple(i) for i in filtered_df.itertuples(index=False, name=None)])

            return store
      

      def update(self, column: str, value: any, id: str) -> None:
            """
            Update column in DB.
            """
            self.cursor.execute(f"UPDATE kmps_db SET {column} = ? WHERE ID = ?", (value,id))


      def create_backup(self) -> None:
            """
            Backup DB to folder.
            """
            self.log.info("Creating a backup of the database.")
            
            # Check how many files are in the Backups folder
            files = len(os.listdir(self.file.path_of_backup_folder()))
            print(files)
            
            # Make backup database
            filename = f"KMPS!db Backup #{files + 1} {datetime.date.today()}.db"
            backup_path = os.path.join(self.file.path_of_backup_folder(), filename)
            shutil.copyfile(self.file.database_pointer(), backup_path)

            self.log.info("Backup created successfully.")


      def switch_database(self) -> None:
            """
            Switch to another DB file.
            """
            try:
                  path = filedialog.askopenfile(initialdir=self.file.path_of_backup_folder()).name
                  
                  # Verify if the user selected the correct file type
                  if not path.endswith(".db"):
                        # Notify the user that the selected file is not of the correct type
                        # error_message()
                        pass
                  else:
                        # Update the database pointer to the selected file
                        self.file.database_pointer(path)
                        self.log.info("Switched database.")
            except:
                  return