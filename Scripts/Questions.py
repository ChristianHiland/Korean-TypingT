import json


def QuestionLevel(Level):
    if Level == 1:
        Q = "Questions 1"
    elif Level == 2:
        Q = "Questions 2"
    elif Level == 3:
        Q = "Questions 3"
    elif Level == 4:
        Q = "Quetions 4"
    elif Level == 5:
        Q = "Questions 5"
    return Q

def Question(Level):
    Total = 0
    Words = "Data/Words.json"
    Show = QuestionLevel(Level)
    with open(Words, "r") as Words:
        Word = json.load(Words)
    
        # Getting the Questions.

        # Level 1
        if Show == str("Questions 1"):
            Q1 = input("What is 'Hello' in Korean? ")
            Q2 = input("What is 'Hi' in Korean? ")
            Q3 = input("What is 'Dog' in Korean? ")
            Q4 = input("What is 'Cat' in Korean? ")
            Q5 = input("What is 'Family' in Korean? ")
            Q6 = input("What is 'Thank You' in Korean? ")
            Q7 = input("What is 'Welcome' in Korean? ")
            Q8 = input("What is 'You' in Korean? ")
            Q9 = input("What is 'I' in Korean? ")
            Q10 = input("What is 'All' in Korean? ")

            if Q1 == Word['Levels']['1']['Q1']:
                Total += 1
            if Q2 == Word['Levels']['1']['Q2']:
                Total += 1
            if Q3 == Word['Levels']['1']['Q3']:
                Total += 1
            if Q4 == Word['Levels']['1']['Q4']:
                Total += 1
            if Q5 == Word['Levels']['1']['Q5']:
                Total += 1
            if Q6 == Word['Levels']['1']['Q6']:
                Total += 1
            if Q7 == Word['Levels']['1']['Q7']:
                Total += 1
            if Q8 == Word['Levels']['1']['Q8']:
                Total += 1
            if Q9 == Word['Levels']['1']['Q9']:
                Total += 1
            if Q10 == Word['Levels']['1']['Q10']:
                Total += 1
    return Total