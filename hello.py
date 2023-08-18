import sys

def hello(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    name = "Anonymous Person"
    if len(sys.argv) == 2:
        name = sys.argv[1]
    hello(name)
