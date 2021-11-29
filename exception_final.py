def func():
    pass
    return

if __name__=='__main__':
    try:
        fh = open('./testfile.txt', 'w')
        fh.write('This is exception finally.')
    except Exception as e:
        pass
    finally:
        fh.close()

pass