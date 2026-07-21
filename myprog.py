def hello(name : str) -> str:
    return f'Hello, {name}!'

print(hello('Reuven'))
print(hello(5))
print(hello([10, 20, 30]))
print(hello(hello))
