#Static Methods
# Methods that don't use the self parameter (work at class level)

class Student:
    @staticmethod #decorator
    def college():
        print("Gitam College")


#Decorators alllow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it