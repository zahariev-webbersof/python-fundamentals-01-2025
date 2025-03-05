for method in dir(str):
    if not method.startswith('__'):
        print(f'🔹 {method}:')
        print(getattr(str, method).__doc__)
        print('-' * 40)