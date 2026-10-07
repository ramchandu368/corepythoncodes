# 1 . counting the function calls
import random
def count_calls(func):  # original generate_ticket function
    function_calls = [0]
    def wrapper():
        function_calls[0]=function_calls[0]+1
        print(f"function calls : {function_calls[0]}")
        return func()
    return wrapper


@count_calls # generate_ticket = count_calls(generate)
def generate_ticket():
    x = random.randint(1000,10000)
    return x

x = generate_ticket()
print("ticket number",x)
x = generate_ticket()
print("ticket number",x)
x = generate_ticket()
print("ticket number",x)
x = generate_ticket()
print("ticket number",x)



