def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("What's n? "))
        if n < 0:
            continue
        else:
            return n

def meow(x):
    for _ in range(x):
        print("Meow!")

main()