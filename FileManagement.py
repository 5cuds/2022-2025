import os
import json
import platform
import getpass
import shutil


class FileManager:
      def __init__(self) -> None:
            """
            Initializes the FileManager class and ensures that the necessary folder structure
            for the KMPS! application is created.
            """
            
            # Create a folder for KMPS!
            self.create_folder()

      def path(self) -> str:
            """
            Determines and returns the base folder path for the KMPS! application
            based on the user's operating system.

            Returns:
                  str: The path to the KMPS! folder.
            """
            try:
                  # Define operating system mappings to identify the current OS
                  os_dict = {
                        "windows": ("Windows", "Windows32", "Windows16"),
                        "mac": ("Darwin", "MacOS"),
                        "linux": ("Linux", "FreeBSD", "NetBSD", "OpenBSD"),
                        "unix": ("AIX", "SunOS", "HP-UX", "IRIX", "Tru64", "UNICOS", "OSF1", "SCO_SV", "UnixWare"),
                        "other": ("Java", "OS/2", "OS/390", "OS/400", "VMS", "BeOS", "Haiku", "QNX", "Inferno", "Plan9", "RISC OS")
                  }

                  # Identify the current operating system
                  current_os = platform.system()
                  if current_os in os_dict["windows"]:
                        folder_path = os.path.join(os.environ['APPDATA'], 'KMPS!')
                  elif current_os in os_dict["mac"]:
                        folder_path = os.path.join(os.environ['HOME'], 'Library', 'Application Support', 'KMPS!')
                  elif current_os in os_dict["linux"]:
                        folder_path = os.path.join(os.environ['HOME'], '.KMPS!')
                  elif current_os in os_dict["unix"]:
                        folder_path = os.path.join(os.environ['HOME'], '.KMPS!')
                  else:
                        # Default to a hidden folder in the user's home directory for unknown OS
                        folder_path = os.path.join(os.environ['HOME'], '.KMPS!')

            except:
                  # Handle any exceptions that occur during path determination
                  # Logging or error handling can be added here
                  pass
            finally:
                  # Ensure the folder path is returned even if an exception occurs
                  return folder_path

      def path_of_backup_folder(self) -> str:
            """
            Returns the path to the backup folder within the KMPS! directory.

            Returns:
                  str: The path to the backup folder.
            """
            return os.path.join(self.path(), "Backups")

      def json_path(self) -> str:
            """
            Returns the path to the JSON settings file within the KMPS! directory.

            Returns:
                  str: The path to the JSON settings file.
            """
            return os.path.join(self.path(), "kmps!_settings.json")

      def create_folder(self) -> None:
            """
            Creates the main KMPS! folder if it does not already exist.
            Also ensures that subfolders and essential files are created.
            """
            try:
                  # Create the main folder if it does not exist
                  if not os.path.exists(self.path()):
                        os.makedirs(self.path(), exist_ok=True)
            except:
                  # Handle any exceptions that occur during folder creation
                  # Logging or error handling can be added here
                  pass
            finally:
                  # Create additional subfolders and files
                  self.create_backups_folder()
                  self.create_readme()
                  self.create_json_file()
                  self.create_log_folder()

      def create_log_folder(self) -> None:
            """
            Creates a folder to store log files within the KMPS! directory.
            """
            path = os.path.join(self.path(), "Logs")

            # Check if the log folder exists
            if not os.path.exists(path):
                  # Create the log folder
                  os.makedirs(path, exist_ok=True)

      def create_backups_folder(self) -> None:
            """
            Creates a folder to store database backups within the KMPS! directory.
            """
            # Check if the backup folder exists
            if not os.path.exists(self.path_of_backup_folder()):
                  os.makedirs(self.path_of_backup_folder(), exist_ok=True)

      def create_json_file(self) -> None:
            """
            Creates a JSON settings file with default settings if it does not already exist.
            """
            # Check if the JSON file already exists
            if not os.path.exists(self.json_path()):
                  # Define default settings
                  json_dict = {"Appearance": "Light",
                              "Auto-Lock": True}
                  
                  # Write the default settings to the JSON file
                  with open(self.json_path(), "w") as file:
                        json.dump(json_dict, file, indent=2)

      def database_pointer(self, update: str = None) -> str:
            """
            Retrieves or updates the database pointer file, which stores the path to the database.

            Args:
                  update (str, optional): The new database path to update. Defaults to None.

            Returns:
                  str: The current database path if no update is provided.
            """
            pointer_path = os.path.join(self.path(), "database_pointer.txt")
            
            # Create the pointer file if it does not exist
            if not os.path.exists(pointer_path):
                  with open(pointer_path, "w") as file:
                        path = os.path.join(self.path(), "KMPS!db.db")
                        file.write(path)
            
            # Read the contents of the pointer file
            with open(pointer_path, "r") as file:
                  contents = file.read()

            # Return the current database path if no update is provided
            if update is None:
                  return contents
            else:
                  # Update the pointer file with the new database path
                  with open(pointer_path, "w") as file:
                        file.write(update)

      def create_readme(self) -> None:
            """
            Creates a README file with a placeholder message in the KMPS! directory.
            """
            name = getpass.getuser()
            text = f"""{name}\nI will do this later"""

            path = os.path.join(self.path(), "README PLEASE!.txt")

            # Create the README file
            with open(path, "w") as file:
                  file.write(text)

      def delete_logs(self) -> None:
            """
            Deletes all log files and the log folder, then recreates the log folder.
            """
            path_log = os.path.join(self.path(), "Logs")
            # Remove the log folder and its contents
            shutil.rmtree(path_log, ignore_errors=True)

            # Recreate the log folder
            self.create_log_folder()
