import os
import shutil


def organize_files():

    enter_path = input("Path: ")

    if os.path.exists(enter_path):
        try:
            for file in os.listdir(enter_path):
                path = enter_path + f"/{file}"
                if os.path.isfile(path):
                    folder_to_make = os.path.splitext(path)
                    type = folder_to_make[1].replace(".", "")

                go_path_yay = enter_path + f"/{type}"
                if not os.path.exists(go_path_yay):
                    os.makedirs(go_path_yay)
                shutil.move(path, go_path_yay)
            print("Done!\n Check Your Folder.")
        except Exception as e:
            print(f"(Exception): {e}")

    else:
        print("The Path Doesn't Exists.")


if __name__ == "__main__":
    organize_files()
