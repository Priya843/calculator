import art
print(art.logo)

def calculator():
  num1=float(input("What is the first number?: "))

  def add(n1, n2):
   return n1 + n2
  def subtract(n1, n2):
   return n1 - n2
  def multiply(n1, n2):
   return n1 * n2
  def divide(n1, n2):
   return n1 / n2

  operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
  } 

  for symbol in operations:
   print(symbol)


  should_continue=True
  while should_continue:

   operation_symbol=input("Pick an operation: ")
   num2=float(input("What is the next number?: "))
   calculation_function=operations[operation_symbol]
   answer=calculation_function(num1,num2)
#print(result)

  print(f"{num1} {operation_symbol} {num2}={answer}")

  if input("Type 'y' to continue calc with {answer} or Type 'n' to restart again") == "y":
   num1=answer
  else:
   should_continue = False
   calculator() #calling this func here will take us to the begnning and ask us to restart it all over again 

calculator()

#print(f"{first_answers} {operation_symbol} {num3}")
 
#print(add(2, multiply(5, divide(8, 4))))

#function=operations["*"]
#function(2,3)