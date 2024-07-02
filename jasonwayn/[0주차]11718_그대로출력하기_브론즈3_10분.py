for i in range(100):
    try:
        a=input()
        print(a)
    except EOFError:
        break