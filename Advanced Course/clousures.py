# Hola 3 -> HolaHolaHola

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo puedes usar cadenas'
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("ja"))

if __name__ == '__main__':
    run()