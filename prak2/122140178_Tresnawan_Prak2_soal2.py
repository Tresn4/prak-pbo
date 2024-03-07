class WithDecorator:
    def __init__(self):
        print("Constructor dipanggil")
        
    def __del__(self):
        print("Destructor dipanggil")

def my_decorator(func):
    def wrapper():
        print("sebelum memanggil fungsi")
        func()
        print("sesudah memanggil fungsi")
    return wrapper

@my_decorator
def my_function():
    print("didalam fungsi")

if __name__ == "__main__":
    obj = WithDecorator() 
    my_function()  

    del obj  
