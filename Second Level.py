     
        def second_level():
    while level>0 and chance>0:
        if not isright:
            chance-=2;
            level++;
          score1= score+10;
            answer=random.choose(answers)
            if answer in answers and needtime=20:
            print("You passed go next level!")
            print(f"Your score is:{score}")
        else:
            chance-=4;
            level;
            score-=10;
            answer=random.choose(answers)
            if answer not in answers:
            print("You failed not go next level!")
