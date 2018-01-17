import requests     #Used to fetch contents of a URL
import html         #Used to decode the imported data from HTML format
import json         #Used to parse the data as a python dictionary
import os           #Used for clearing screen
import csv          #Used to save data to leaderboards
from random import shuffle   #Used to shuffle the options
from operator import itemgetter   #Used for leaderboard purposes
link = "https://opentdb.com/api.php?amount="    #API used in this program
name=input("Enter your name - :")
num=input("Choose no. of questions(max 50) - ")
multi={'hard':3, 'medium':2, 'easy':1}    #Multiplier for score
link = link+str(num)
diff=input("Choose difficulty of questions(easy, medium, hard, random) - ")
diff=diff.lower()
leaderboard=[]
score=0
if diff not in ['easy','medium','hard']:
    print("Choosing Random difficulty")
else:
    link=link+"&difficulty="+diff
print("Loading Questions")
f = requests.get(link)     #Fetching data from API
json_data=f.text           #Converting to string
quiz= json.loads(json_data) #Converting string to dictionary
for questions in quiz["results"]:
    os.system('cls')
    answers=[]
    for i in range(0,len(html.unescape(questions["question"]))-1):  #HTML Decode along with printing the question
        print("-",end='')
    print("-")
    print(html.unescape(questions["question"]))
    print("Difficulty- ",questions["difficulty"])                   #Shows difficulty of question
    for i in range(0,len(html.unescape(questions["question"]))-1):
        print("-",end='')
    print("-")
    for incorrect in questions["incorrect_answers"]:                #Appending possible answers in a separate dictionary
        answers.append(incorrect)                                   #and shuffling them
    answers.append(questions["correct_answer"])
    shuffle(answers)
    mcq=['a','b','c','d']
    mcq=dict(zip(mcq,answers))
    for x in mcq:
        print(html.unescape(x),'-',html.unescape(mcq[x]))
    #print(questions["correct_answer"])                             #Remove # to show correct answers in output along with answer bank
    ans=input("Ans - ")
    ans=ans.lower()
    if mcq[ans] in questions["correct_answer"]:
        print("Correct Answer")
        score=score+5*(multi[questions["difficulty"]])              #Points allocation for correct answer
    else:
        print("Wrong Answer")
        print('Correct Answer- '+questions["correct_answer"])              
    print("Total Score till now - ",score)                          #Shows total score after every question
    input("Press any key for the next question")
print("Quiz Over")
print("Total Score - ",score)
print("Press enter to see leaderboards")
os.system('cls')
with open('Leaderboard.csv', 'a', newline='') as file:              #Saving current game score to leaderboards
    writer = csv.writer(file)
    writer.writerow((score, name))
                
with open('Leaderboard.csv', 'r', newline='') as file:              #Importing leaderboards for high scores
    score_list = list(csv.reader(file))
    for row in score_list:
        leaderboard.append(row)
leaderboard=sorted(leaderboard, key=itemgetter(0), reverse= True)   #Sorting leaderboards by descending order according to score
print('Name \t Score')
for x in leaderboard:
    print(x[1] + '\t' + x[0])                                       #Print the leaderboard
input("Press any key to exit")
