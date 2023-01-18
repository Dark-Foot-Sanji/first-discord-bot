import random

def get_ressponse(message: str) -> str:
    p_message = message.lower() 
    
    if p_message == 'hello':
        return 'Hey There!'
