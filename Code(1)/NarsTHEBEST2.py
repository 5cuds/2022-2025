the_best = "JustNars"
the_count = 0
the_limit = 1
while the_count < the_limit:
    i = input('''who is the best bedwars player?
1)eliminator
2)itzMQ
3)JustNars
4)lawra
Put here: ''')
    the_count += 1
    if i == the_best:
        print("Correct!")
        break
else:
    print("Incorrect")