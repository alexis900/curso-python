from datetime import datetime
import pytz

#FILE = './files/timezones.txt'

def gen_file(file: str) -> None:
    def generate_file(func: list[str]) -> None:
        def wrapper(*args, **kwargs) -> None:
            with open(file, 'w', encoding='utf-8') as f:
                my_list = func(*args, **kwargs)
                for i in my_list:
                    f.write(f'{i}\n')
            f.close()
        return wrapper
    return generate_file

#@gen_file(FILE)
def timezones() -> list[str]:
    timezone_list = [tz for tz in pytz.all_timezones]
    return timezone_list

def list_grantimezones(tz: list[str]) -> list[str]:
    my_list: list[str] = []
    for i in tz:
        i = i.split('/')
        if i[0] not in my_list:
            my_list.append(i[0])
    return print(my_list)

def list_subregion(tz: list[str], zone: str) -> list[str]:
    region_list = [i for i in tz if zone in i]
    my_list: list[str] = []
    for i in region_list:
        try:
            i = i.split('/')
            my_list.append(i[1])            
        except IndexError:
            continue
    return print(my_list)

def run() -> None:
    tz = timezones()
    list_grantimezones(tz)
    gz = str(input('Seleccione una zona geográfica: '))
    list_subregion(tz, gz)
    gsz = str(input('Seleccione la sub-zona geográfica: '))
    time = pytz.timezone(str(f'{gz}/{gsz}'))
    print(datetime.now(time))
    




if __name__ == '__main__':
    run()