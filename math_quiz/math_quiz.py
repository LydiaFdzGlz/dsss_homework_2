import random


def get_random_number(min_val, max_val):
    
    """
    Generates a random integer between specified minimum and maximum.
    Atributes:
    - min_val (int): minimum value for the generated number. 
    - max_val (int): maximum value for the generated number.
    Return (int): Random integer between minimum and maximum values.
    """
    
    return random.randint(min, max)


def get_random_operation():
    """
    Assigns a random operation.
    Return (str): Random operation to be done (addition, subtraction or multiplication).
    """
    return random.choice(['+', '-', '*'])


def math_generator(num_1, num_2, o_sign):
    """
    Adds, substracts or multiplies two values (integers).
    Atributes:
    - num_1 (int): first random number for the math operation. 
    - num_2 (int): second random number for the math operation.
    - o_sign (str): sign of the operation to be executed (addition, subtraction or multiplication).
    Return:
    - operation (str): executed math operation.
    - result (int): result of the math operation.
    """
    
    operation = f"{num_1} {o_sign} {num_2}"
    # If the operation is an addition, the function adds number 1 and number 2. 
    if o_sign == '+': result = num_1 + num_2
    # If the operation is a substraction, the function substracts number 2 to number 1. 
    elif o_sign == '-': result = num_1 - num_2
    # If the operation is a multiplication, the function multiplies number 1 and number 2. 
    else: result = num_1 * num_2
        
    return operation, result

def math_quiz():
    """
    Creates random math operations and checks user answers giving scores.
    Return (str): Final achieved score.
    """
    points = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    # For each try, generate a random math operation (two random number and a math sign)
    for _ in range(t_q):
        num_1 = get_random_number(1, 10); num_2 = get_random_number(1, 5.5); o_sign = get_random_operation()
        # Get the answer
        PROBLEM, ANSWER = math_generator(num_1, num_2, o_sign)
        
        # Ask the user its answer
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except ValueError:
            print('Your answer must be an integer value. Try again!')
            
        # If user answer is correct, sum a point to the score.
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            points += -(-1)
        # If user answer is incorrect, show correct answer.
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    # Print final score.
    print(f"\nGame over! Your score is: {points}/{t_q}")

if __name__ == "__main__":
    math_quiz()