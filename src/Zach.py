

def get_name():
    return "Mike"

def main():
    name = ["Zach", "Will", "Ellie"]
    for n in name:
        #m = get_name()
        print(f"Hello {n} and {get_name() + ' and James'}")


if __name__ == "__main__":
    main()