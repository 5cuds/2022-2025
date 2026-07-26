import string, itertools, time


def BruteForce(password: str) -> None:
      """Brute Force Password"""

      chars = string.ascii_letters + string.digits + string.punctuation
      attempts = 0
      start = time.time()
      
      for l in range(len(password) + 1):
            for i in itertools.product(chars, repeat=l):

                  print(f"Attempts: {attempts}", end="\r")
                  #print(i)
                  attempts += 1

                  guessed_password = "".join(i)

                  if guessed_password == password:
                        print(f"\nCracked Password!\nPassword: {guessed_password}")
            
                        stop = time.time()
                        timetook = stop - start
                        
                        print(f"Time Took: {timetook:.2f}")
                        print(f"Attempts InTotal: {attempts}")

                        return

def DictCracker(password: str, file: str) -> str:
      """Dictionary Attack"""
      pass


def main() -> None:
      print("1.Brute Force\n2.Dictionary Attack")

      match input("> "):
            case "1":
                  password = input("Password To Crack: ").strip()
                  BruteForce(password=password)
            
            case "2":
                  file_path = input("File Path Of Dictionary: ")
                  password = input("Password: ")
                  DictCracker(password=password, file=file_path)

            case _: 
                  print("Invalid Choice!")
                  main()

if __name__ == "__main__":
      main()