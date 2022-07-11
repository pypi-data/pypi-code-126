


from io import StringIO






def menu(**kwargs):

    
    while True:
        s = input("Enter input: ")


        if s in kwargs:
            return kwargs[s]()

        print("Invalid input. Try Again!")





'''
def test_menu(monkeypatch):
    def func_a():
        return 'A'

    def func_b():
        return 'B'
    monkeypatch.setattr('builtins.input',lambda _: "a")


    assert menu(a=func_a) == 'A'
'''



