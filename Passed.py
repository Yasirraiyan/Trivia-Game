def passed(fail):
        if not fail:
            score=score1+score2+score3+score4+score5;
            print(f"You win.Your score is:{score}")
        if fail and score==0:
            fail==True
             print(f"You Fail.Your score is:{score}")
