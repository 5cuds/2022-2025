import requests

def get_quiz() -> dict:
      """Get Quizs From An API"""
      req = requests.get("https://the-trivia-api.com/api/questions?limit=10")

      # check if status code is 200
      if req.status_code == 200:

            # convert to json format
            data = req.json()

            # this dict just stores Questions and answers in a key-value pair
            quiz_dict = {
                  "Category": data[0]["category"],
                  "Answer": data[0]["correctAnswer"],
                  "Choices": data[0]["incorrectAnswers"] + [data[0]["correctAnswer"]],
                  "Question": data[0]["question"].title()
            }

            return quiz_dict
      
      else:
            print(f"Status Code: {req.status_code}")
      

def main() -> None:
      while True:
            try:

                  for _ in range(6):
                        quiz_dict = get_quiz()
                        print(f"{quiz_dict["Question"]}\n{"="*15}")

                        for index, choice in enumerate(quiz_dict["Choices"]):
                              print(f"{index}){choice}")

                        print("="*15)

                        
                        users_answer = int(input("> "))

                        if users_answer > 4:
                              print("Invalid Answer!")
                              continue

                        if quiz_dict["Choices"][users_answer] == quiz_dict["Answer"]:
                              print("Correct!")

                        else:
                              print("Incorrect") 

                        print()                   
                  

            except ValueError:
                  print("Numbers Values ONLY!")
                  continue
            

if __name__ == "__main__":
      main()
