import os

def test():
    print(os.getcwd())
    if os.getcwd() != 'd:\mole\image':

            os.chdir("image")

    test()



if __name__ == "__main__":

    test()