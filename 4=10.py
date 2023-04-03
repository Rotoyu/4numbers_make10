import random as r
from itertools import product

def make_number_list():
    results=[]
    for c in product(range(10), repeat=4): #makes every possible outcome of 4 numbers, from 0~9, which can be repeatable.
        results.append(list(c))
    r.shuffle(results)
    one_question=results.pop() #takes one out of the list
    return one_question

def make_operation_list():
    results_pos=[] 
    results_neg=[] 
    for c in product('+-*/', repeat=3): #makes every possible outcome of 4 operators, which can be repeatable.
        results_pos.append(list(c))
        results_neg.append(list(c))
    
    for x in range(len(results_pos)):
        results_pos[x].insert(0,'+') #makes first operation +
        results_neg[x].insert(0,'-') #makes first operation -
    
    big_list = [] #Combined list
    big_list = results_neg + results_pos #Combining lists
    r.shuffle(big_list)
    return big_list

def check_combinations(op_list, num_list): #check if list is valid
    correct_answer_lists=[]
    for miniop in op_list:
        final_string = ''
        if len(miniop) == 4:
           for x in range(4):
                number = str(num_list[x])
                operator = str(miniop[x])
                final_string += operator + number #Combine strings
        if '/0' in final_string: #Avoid zero division error
            continue
        if eval(final_string) == 10 and (len(final_string) == 8): #Calculation, checking calculation
            correct_answer_lists.append(final_string)
    return correct_answer_lists
                            
def check_answer(user_answer, answer):
    if str(user_answer) in answer: #Checks if user's answer is in the list of answers
        return True
    else:
        return False

def make_question():
    num_list = make_number_list() #makes all combinations of numbers, pops one
    op_list = make_operation_list() #makes all combinations of operations
    answer=check_combinations(op_list,num_list) #combines them until one that makes 10 is found
    placeholder=1
    while placeholder==1:
        if answer != []:
            placeholder=0
        else:
            num_list = make_number_list() #makes all combinations of numbers, pops one
            answer=check_combinations(op_list,num_list) #combines them until one that makes 10 is found
    return num_list, answer

def main():
    print("*"*50)
    print('Welcome to 4=10, the Kanari version!')
    print('Here are the rules:')
    print('1) You will be given 4 numbers, and using the 4 operators +, -, *, and /, you will try to make the answer "10"')
    print('2) You are NOT able to rearrange the numbers.')
    print('3) Certain calculations have priorities. Like "*" and "/" go before "-" and "+".')
    print("4) Write the answer in the format _x_x_x_x. Ex: +1-2*3/4 ")
    print("5) The first digit may be negative or positive. If it's positive, put a + sign in front of the number")
    print('6) All problems are solvable. Good luck!')
    print('*'*50)
    x=1
    new_question = 'y'
    while new_question == 'y':
        num_list, answer = make_question()
        user_answer=''
        check = True
        play = 'c'
        print(f"Question #{x}")
        while play == 'c' or check == True:
            print(f"Your list of numbers is: {num_list}")
            user_answer=input("Your answer: ")
            check=check_answer(user_answer, answer)
            if check == True:
                print('\nCorrect!')
                False
                break
            else:
                print('Wrong! Try again.')
            play = input('Type "c" to keep trying or "g" to giveup on this question.')
            if play == 'q':
                break
        print(f"All possible answers: {answer}")
        new_question=input("\nType 'y' to play another question. Type anything else to quit. ")
        if new_question == 'y':
            x+=1
        else:
            print('Thanks for playing!')
        print('*'*50)
main()