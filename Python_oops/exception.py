

# ZeroDivisionError
# ValueError
# ModuleNotFoundError
# ImportError
# IndentationError
# IndexError
# NameError
# KeyError

# try:
#     # Code that may raise an exception
#     result = 10 / 0
# except ZeroDivisionError as e:
#     # Handling the exception
#     print("Error: Division by zero is not allowed.")
#     print(f"Exception details: {e}")
# else:
#     # This block executes if no exceptions are raised
#     print("Division successful, result is:", result)
# finally:
#     # This block always executes, regardless of an exception occurring or not
#     print("Execution of the try-except block is complete.")



# class CustomError(Exception):
#     """A custom exception class"""
#     pass

# def divide(a, b):
#     if b == 0:
#         raise CustomError("Custom Error: Denominator cannot be zero.")
#     return a / b

# try:
#     num1 = 10
#     num2 = 0
#     print("Attempting to divide", num1, "by", num2)
#     result = divide(num1, num2)
# except ZeroDivisionError as e:
#     print("Error: Division by zero is not allowed.")
#     print(f"Exception details: {e}")
# except CustomError as e:
#     print(f"Caught a custom exception: {e}")
# except TypeError as e:
#     print("Error: Invalid data type encountered.")
#     print(f"Exception details: {e}")
# except Exception as e:
#     # Catching all other exceptions
#     print("An unexpected error occurred.")
#     print(f"Exception details: {e}")
# else:
#     print("Division successful, result is:", result)
# finally:
#     print("Execution of the try-except block is complete.")



class Usererror(Exception):
    pass

def hi(a,b):
    if b==0:
        # raise Usererror("user create kiya huva...")
        pass
    
    else:
        print("solve huva na")


    
try:
    a=1
    b=0
    hi(a,b)
# except IndexError as i:
#     print(i)
except Exception as e:
    print(e)
finally:
    print("try and except executed barabar")


            
