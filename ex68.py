# stworzcie funkcje HelloWorld
# stworz dekorator ktory bedize informowal o rozpoczeciu i zakonczeniu wykonywania
# dekorowanej funkcji

def inform_about_fun_start_and_stop(fun):
    def inner():
        print("Start")
        fun()
        print("Stop")
    return inner

@inform_about_fun_start_and_stop
def hello_world():
    print("HelloWorld")

hello_world()
