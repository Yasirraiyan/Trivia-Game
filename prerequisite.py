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
