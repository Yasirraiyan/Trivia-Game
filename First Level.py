def first_level():
    while level>0 and chance>0:
        if not isright:
            chance--;
            level++;
          score1= score+5;
            answer=random.choose(answers)
            if answer in answers and needtime==10:
            print("You passed go next level!")
        else:
            chance-=2;
            level;
            score-=5;
            answer=random.choose(answers)
            if answer not in answers:
            print("You failed not go next level!")
            
