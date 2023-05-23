import random
from .models import CodeActivate


def generate_activation_code(user):
    '''
        Generate Activation Code for User
    '''
    code = ""
    for _ in range(5):
        digit = random.randint(0, 9)
        code += str(digit)

    store_activation_code(user=user, activation_code=code)

    return code

def store_activation_code( user, activation_code):
    '''
        Store Activation Code into Code Activation Model
    '''
    # Create a new instance of CodeActivate model and save the activation code
    code = CodeActivate(user=user, code=activation_code)
    code.save()
    
    
# Check Code Activation For user
def check_activation_code( code):
    '''
        Check if user code enter equal of Code Activation or Not
    '''
    active_code = CodeActivate.objects.filter(code = code).last()
    if active_code:
        user = active_code.user
        CodeActivate.objects.filter(user = user).all().delete()
        return user
    return None