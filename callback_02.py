def fun_callback(input):
    print('fun_callback sum: ',input)
    return

def fun_call(one, two, f_callback):
    result = one + two
    f_callback(result)
    return

first = 10
second = 20
fun_call(first, second, fun_callback)