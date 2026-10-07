#third question

def process_data(func):  # original calculate_function
    def wrapper(*args):
        x = func(*args) #x=[]
        l = list(filter(lambda x:x>40,x))
        l = list(map(lambda x:x+5,l))
        l = sorted(l,reverse=True)
        return l
    return wrapper


@process_data  # calculate_scores = process_data(calculate_data)
def calculate_scores(*args):
    return list(args)
print(*calculate_scores(80,22,45,65,70,95))