#Author: Johan Guerrero-Avitia
def main():
    """
    This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters (D,d,a,A).
    Depending on the result the computer shows, we will display a different message.
    """
    print("Answer the following question Consider that: \n Strongly Disagree: D \n Disagree: d \n Agree: a \n Strongly Agree:A")
    score=0
    #Here we are separating the positive questions from the negative ones using the fuctions
    score+=positive_question(input("I feel that I am a person of worth, at least on an equal plane with others."))
    print()
    score+=positive_question(input("I feel that I have a number of good qualities."))
    print()
    score+=negative_question(input("All in all, I am inclined to feel that I am a failure."))
    print()
    score+=positive_question(input("I am able to do things as well as most other people."))
    print()
    score+=negative_question(input("I feel I do not have much to be proud of."))
    print()
    score+=positive_question(input("I take a positive attitude toward myself."))
    print()
    score+=positive_question(input("On the whole, I am satisfied with myself."))
    print()
    score+=negative_question(input("I wish I could have more respect for myself."))
    print()
    score+=negative_question(input("I certainly feel useless at times."))
    print()
    score+=negative_question(input("At times I think I am no good at all."))
    print()
    print(f"Your score is: {score} \nA score below 15 may indicate problematic low self-esteem.")

def positive_question(question):
    """
    Here we will assign the score depending on the answer they typed previously
    notice that the postive question have different scores than the negative ones
    """
    if question == "D":
        score = 0
    elif question == "d":
        score = 1
    elif question == "a":
        score = 2
    elif question == "A":
        score = 3
    return score

def negative_question(question):
    """
    Here we will assign the score depending on the answer they typed previously
    notice that the negative question have different scores than the postive ones
    """
    if question == "D":
        score = 3
    elif question == "d":
        score = 2
    elif question == "a":
        score = 1
    elif question == "A":
        score = 0
    return score
main()
