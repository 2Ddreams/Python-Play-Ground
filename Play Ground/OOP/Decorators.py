#   def outter_function(msg):
#       def inner_function():
#           print(msg)
#       return inner_function
#   
#   hi_func = outter_function("hi")
#   bye_func = outter_function("bye")
#   
#   hi_func()
#   bye_func()



def decorator_function(origiral_function):
    def wrapper_function():
        return origiral_function()
    return wrapper_function

def display():
    print(f"Display function ran")

decorated_display = decorator_function(display)


decorated_display()