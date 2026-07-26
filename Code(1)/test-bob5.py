print('''Hello there! im bob if u need help if your Cold or very warm im here to help! my commands 
are (Im Cold) and (Im Very warm) or (none) to terminate the program''')

command = input("Put here: ")

if command.lower() == "im cold":

    print('''1)Blow warm air onto cold hands.
2)Tuck hands or feet inside warm clothing next to bare skin. ...
3)Cup cold ears with warm hands.
4)Put cold hands, feet, or ears in warm (not hot) water for 15 to 30 minutes. ...
5)Warm towels can be used to warm the genital 
area but be careful not to burn the skin.''')
    
elif command.lower() == "im very warm" or "im warm":

    print('''
1)Drink cool liquids. ...
2)Go somewhere with cooler air. ...
3)Get in cool water. ...
4)Apply cold to key points on the body. ...
5)Move less. ...
6)Wear lighter, more breathable clothing. ...
7)Take heat regulating supplements. ...
8)Talk to a doctor about thyroid health.''')
    
elif command =='none':

    exit()

else:
    
    print("i don't understand that")
