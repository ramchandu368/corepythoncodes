from traceback import print_tb


def check_access(func):
    def wrapper(username,role):
        if username and role=="admin" or role=="manager":
            return func(username,role)
        else:
            print("Access Denied")
    return wrapper


@check_access  # view_report = check_access(view_report)
def view_report(username,role):
    print("this is the report")

view_report("ramchandu","manager")
