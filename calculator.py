def add(num1, num2):
  return num1 + num2

def sub(num1, num2):
  return num1 - num2


def mul(num1, num2):
  return num1 * num2


def div(num1, num2):
  return num1 / num2

operators = {"+" : add,
             "-" : sub, 
             "*" : mul,
             "/" : div
            }
def calculation():
  num1 = float(input("Whats the first number?: "))
  for operator in operators:
    print(operator)
  should_continue = True
  while should_continue:
    choose_operator = input("Pick one operator : ")
    num2 = float(input("Whats the second number?: "))
    calculation_function = operators[choose_operator]
    answer = calculation_function(num1, num2)
    print(f"{num1} {choose_operator} {num2} = {answer}")
    if input("Type 'y' to continue calculation and type 'n' to stop and starts from new calculation: ") == "y":
  #for_continuation = input("Type 'y' to continue calculation with type 'n' to get new calculation: ")
  #  if for_continuation == "y":
      num1 = answer
    else:
      should_continue = False
      calculation()

calculation()
