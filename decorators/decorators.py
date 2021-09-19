def add_action_status(func):
    def inner(*args, **kwargs):
        f = func(*args, **kwargs)
        print('Action finished successfully!')
        return f
    return inner