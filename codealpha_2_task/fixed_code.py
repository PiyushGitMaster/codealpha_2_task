import ast

import os

def load_configuration(data):
    # Unsafe evaluation of user data
    settings = ast.literal_eval(data)
    return settings

result = load_configuration("{'theme': 'dark'}")
print(result)
