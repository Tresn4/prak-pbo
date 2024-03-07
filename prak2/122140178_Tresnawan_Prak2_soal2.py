def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator: Before method execution")
        result = func(*args, **kwargs)
        print("Decorator: After method execution")
        return result
    return wrapper

class MyClass:
    @my_decorator
    def __init__(self, name):
        print(f"Constructor: Object {name} is created.")

    def my_method(self):
        print("Method: Executing my_method")

    def __del__(self):
        print("Destructor: Object is destroyed.")

obj = MyClass("Object1")

obj.my_method()

# Objek akan dihapus secara otomatis setelah tidak digunakan lagi