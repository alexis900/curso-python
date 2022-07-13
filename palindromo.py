def palyndrom(word):
    word = word.replace(' ', '').lower()
    
    if word[::] == word[::-1]:
        return True

def run():
    word = input("Escribe una palabra: ")
    is_palyndrom = palyndrom(word)
    if is_palyndrom == True:
        print("Is a palyndrom")
    else:
        print("Is not a palyndrom")


if __name__ == '__main__':
    run()