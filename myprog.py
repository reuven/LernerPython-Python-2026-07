from typing import Any

def hello(name : str) -> str:
    return f'Hello, {name}!'

print(hello('Reuven'))
print(hello(5))
print(hello([10, 20, 30]))
print(hello(hello))

def add(first, second):
    return first + second

print(add(10, 3))
print(add('a', 'b'))
print(add('a', 5))
