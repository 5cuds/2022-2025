from LoggingConfig import Log
import os
import json
import platform
import getpass
import shutil

class FileManager:
      def __init__(self) -> None:
            """
            Init FileManager, make folders.
            """
            
            # Create a folder for KMPS!
            self.create_folder()

            self.log = Log("File Mangement")
            

      def path(self) -> str:
            """
            Get KMPS! folder path.
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
            Get backup folder path.
            """
            return os.path.join(self.path(), "Backups")

      def json_path(self) -> str:
            """
            Get JSON settings file path.
            """
            return os.path.join(self.path(), "kmps!_settings.json")

      def create_folder(self) -> None:
            """
            Make KMPS! folder and subfolders.
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
            Make log folder.
            """
            path = os.path.join(self.path(), "Logs")

            # Check if the log folder exists
            if not os.path.exists(path):
                  # Create the log folder
                  os.makedirs(path, exist_ok=True)

      def create_backups_folder(self) -> None:
            """
            Make backup folder.
            """
            # Check if the backup folder exists
            if not os.path.exists(self.path_of_backup_folder()):
                  os.makedirs(self.path_of_backup_folder(), exist_ok=True)

      def create_json_file(self) -> None:
            """
            Make JSON file with default settings.
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
            Get or update DB pointer file.
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
            Make README file.
            """
            name = getpass.getuser()
            text = f"""{name}\nI will do this later"""

            path = os.path.join(self.path(), "README PLEASE!.txt")

            # Create the README file
            with open(path, "w") as file:
                  file.write(text)

      def delete_logs(self) -> None:
            """
            Delete all logs and recreate log folder.
            """
            path_log = os.path.join(self.path(), "Logs")
            # Remove the log folder and its contents
            shutil.rmtree(path_log, ignore_errors=True)

            # Recreate the log folder
            self.create_log_folder()
