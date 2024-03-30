def main():
    """
    """
    y = input("What would you like to yell?")
    w = input("What would you like to whisper?")
    d = input("What would you like to day dream about?")
    
    #Print the result to the user.
    print(yelling(y))
    print(whisper(w))
    print(day_dreaming(d))

def yelling(sentence):
    return sentence.upper()
def whisper(sentence):
    """
    Lower case sentence
    Parameters:
    sentences(str): The sentence to lowercase.
    Returns:
    str: The sentences turn into lowercase
    """
    return sentence.lower()
def day_dreaming(sentence):
    return(f"*{sentence}*")
main()