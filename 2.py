def perform_division(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ArithmeticError as e:
        print(f"Arithmetic Error occurred: {e}")

perform_division(10, 2)  
perform_division(10, 0) 
