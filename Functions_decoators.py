def decorated_by(func):
    func.__doc__ += '\nDecorated by decorated_by.'
    return func

def also_decorated_by(func):
    func.__doc__ += '\n also Decorated by decorated_by.'
    return func
'''
def add(x, y):
    """Return the sum of x and y."""
    return x + y
'''
@also_decorated_by
@decorated_by
def add(x, y):
    """Return the sum of x and y."""
    return x + y

if __name__ == '__main__':
    #add = decorated_by(add)
    print help(add)
    
