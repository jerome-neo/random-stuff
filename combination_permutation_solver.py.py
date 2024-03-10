from itertools import combinations, permutations
import re


def generate_combination_permutations(size):
    if size < 1 or size > 9:
        raise ValueError("Size should be between 1 and 9.")
    
    numbers = list(range(1, 10))
    combinations_list = list(combinations(numbers, size))
    
    permutations_list = []
    for combo in combinations_list:
        perms = list(permutations(combo))
        permutations_list.extend(perms)
    
    return permutations_list

def ans(string):
    string, ans = string.split("=")
    ans = int(ans)
    size = string.count(".")
    guess = generate_combination_permutations(size)

    for g in guess:
        equation = string
        for value in g:
            equation = re.sub(r'\.', str(value), equation, count = 1)
        try:
            result = eval(equation)
            if result == ans:
                print(f"The equation {equation} is satisfied.")
                print("\033[1m" + str(g) + "\033[0m")
                break
            else:
                continue
        except Exception as e:
            print(f"Error evaluating the equation: {e}")    

while True:
    print("Enter 'done' to terminate the program")
    user_input = input("Key in . for unknown values: ")
    if user_input.lower() == 'done':
        break
    else:
        ans(user_input)