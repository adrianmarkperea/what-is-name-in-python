def greet(name):
    print(f'Hi, {name}!')

print('__name__ is:', __name__)

if __name__ == '__main__':
    while True:
        print("What's your name?")
        name = input('> ')

        if name == 'q':
            break

        greet(name)
