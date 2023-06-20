indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }

def degree(a: int):
    degrees = ""
    temp = str(a)
    for char in temp:
        degrees += indexes[char] or ""
    return "a = " + temp + degrees


if __name__ == "__main__":
    print(degree(1024))
    print(degree(-1024))
    print(degree(int(input("Введите число: "))))