a = 50 
b = 20
c = 10
d = 0

def add():
    return a + b

def mul():
    return c * d

def div():
    return c / d

if __name__=='__main__':
    try:
        add()
        mul()
        div()


    except ZeroDivisionError:
        d = 1
        pass
    except Exception as e:
        pass
