from art import logo # seperate ascii art - not included in here
print(logo) # separate ascii art - not included

# Create the functions for the operations

# Add
def add(n1, n2):
    return n1 + n2
# Subtract
def subtract(n1, n2):
    return n1 - n2
# Multiply
def multiply(n1, n2):
    return n1 * n2
# Divide
def divide(n1, n2):
    return n1 / n2

# put the above operations into a dictionary
# Keys are each of these symbols that we've used to add/subtract etc
# values are the names of the functions

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# create the calculator function
def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        # introduce a while loop that either restarts the function or continues using the previous number
        keep_going = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()     
        #clear()
        if keep_going == "n":
            should_continue = False
            calculator()
            #clear()
        else:
            num1 = answer

# call the calculator function the first time
calculator()
