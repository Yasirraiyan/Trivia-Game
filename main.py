import random
import time
level=5;
chance=5;
score=0;
bool isright=False
bool iswrong=True;
starttime=time.time;
endtime=time.time;
needtime=endtime-starttime;
bool fail=False;
questions = [
    "What is the capital of France?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for water?",
    "Who painted the Mona Lisa?"
]
answers = [
    "Paris",
    "William Shakespeare",
    "Jupiter",
    "H2O",
    "Leonardo da Vinci"
]
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
         
        def third_level():
    while level>0 and chance>0:
        if not isright:
            chance-=2;
            level++;
          score1= score+15;
            answer=random.choose(answers)
            if answer in answers and needtime==30:
            print("You passed go next level!")
            print(f"Your score is:{score}")
        else:
            chance-=8;
            level;
            score-=15;
            answer=random.choose(answers)
            if answer not in answers:
            print("You failed not go next level!")
                  
        def fourth_level():
    while level>0 and chance>0:
        if not isright:
            chance-=2;
            level++;
          score1= score+20;
            answer=random.choose(answers)
            if answer in answers and needtime=40:
            print("You passed go next level!")
            print(f"Your score is:{score}")
        else:
            chance-=16;
            level;
            score-=20;
            answer=random.choose(answers)
            if answer not in answers:
            print("You failed not go next level!")
                  
        def fifth_level():
    while level>0 and chance>0:
        if not isright:
            chance-=32;
            level++;
          score1= score+25;
            answer=random.choose(answers)
            if answer in answers and needtime=50:
            print("You passed go next level!")
            print(f"Your score is:{score}")
        else:
            chance-=32;
            level;
            score-=30;
            answer=random.choose(answers)
            if answer not in answers:
            print("You failed not go next level!")
            
    def passed(fail):
        if not fail:
            score=score1+score2+score3+score4+score5;
            print(f"You win.Your score is:{score}")
        if fail and score==0:
            fail==True
             print(f"You Fail.Your score is:{score}")
         def fail(fail):
        if  fail:
            score=score1+score2+score3+score4+score5;
            print(f"You fail.Your score is:{score}")
        if fail and score==0:
            fail==False
             print(f"You Fail.Your score is:{score}")
        
    
