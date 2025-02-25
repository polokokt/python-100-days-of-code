def greet():
    print("Hello")
    print("How do you do?")

greet()

def greate_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greate_with_name("Rafal")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Rafal", "Warszawa")   # Positional argument call
greet_with(location="Legionowo", name="Andrzej")  # Keyword argument call
