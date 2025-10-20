#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_positive_int():
    """Prompt user until they enter a valid positive integer"""
    while True:
        user_input = input("How many Fibonacci terms do you want? ")
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        else:
            print("Invalid input. Please enter a positive integer.")

def generate_fibonacci(n):
    """Return a list containing n terms of the Fibonacci sequence"""
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a+b
    return fib

def print_sequence(seq):
    """Print the Fibonacci sequence nicely"""
    print("Fibonacci sequence:")
    print(", ".join(map(str, seq)))

# --- MAIN PROGRAM ---
terms = get_positive_int()
sequence = generate_fibonacci(terms)
print_sequence(sequence)
