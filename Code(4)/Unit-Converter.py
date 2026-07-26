class UnitProgram:

    def f_c(self):
        print("=================")
        while True:
            c_f_input = input("(Celsius/Fahrenheit)? >> ").capitalize().strip()

            if c_f_input == "Celsius" or  c_f_input == "Fahrenheit":
                    while True:
                        if c_f_input == "Celsius":
                             temp = int(input(f"Enter a Temperature in Fahrenheit: "))
                             converted_temp = (temp - 32) * 5 / 9 
                             print(f"Converted Temperature (F-C): {round(converted_temp)}°C")
                        else:
                            temp_f = int(input(f"Enter a Temperature in Celsius: "))   
                            converted_temp_f = temp_f * 9 / 5 + 32 
                            print(f"Converted Temperature (C-F): {round(converted_temp_f)}°F")
                        return
            else:
                print("Enter a valid choice.")
                continue
            

    def m_k(self):
        print("=================")
        while True:
            m_k_input = input("(Miles/Kilometers)? >> ").capitalize().strip()

            if m_k_input == "Miles" or  m_k_input == "Kilometers":
                    while True:

                        if m_k_input == "Miles":
                             distance = int(input(f"Enter a Distance in Kilometers: "))
                             converted_distance  = distance * 1.60934 
                             print(f"Converted Distance (K-M): {converted_distance} Miles")

                        else:
                            distance_k = int(input(f"Enter a Distance in Miles: "))   
                            converted_distance_k = distance_k / 1.60934 
                            print(f"Converted Distance (M-K): {converted_distance_k} Kilometers")
                        return
                        
            else:
                print("Enter a valid choice.")
                continue

def main():
    try:
        d = UnitProgram()
        while True:
            print("Python Unit Converter\n=================")
            print("1)Miles, Kilometers\n2)Fahrenheit, Celsius\n3)Exit\n=================")

        
            user_input = int(input("> "))
            
            if user_input == 1:
                d.m_k()
            elif user_input == 2:
                d.f_c()
            elif user_input == 3:
                exit()
            else:
                print("Enter a valid choice.")
                return

    except Exception as e:
         print(f"Error: {e}")
if __name__ == "__main__":
    main()
