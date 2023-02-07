import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is deciededly so.'
    elif answerNumber == 3:
        return 'A future is bright.'
    elif answerNumber == 4:
        return 'The sky is the limit.'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Oh my friend, you just found it.'
    elif answerNumber == 7:
        return 'Check your pocket, sir.'
    elif answerNumber == 8:
        return 'Outlook not so good.'
    elif answerNumber == 9:
        return 'Be patient you are almost there.'
    else:
        return 'Gotcha!'
 
# r = random.randint(1,11)
# fortune = getAnswer(r)
# print(fortune)

# Equivalent one line. 
print(getAnswer(random.randint(1,11)))