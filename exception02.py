def add():
    a = 50 
    b = 20
    return a + b

def mul():
    c = 10
    d = 0
    return c * d

def div():
    c = 10
    d = 0
    return c / d

if __name__=='__main__':
    try:
        print(add())
        print(mul())
        print(div())


    except ZeroDivisionError:
        d = 1
        pass
    except Exception as e:
        pass
