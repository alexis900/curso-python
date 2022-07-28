def remove_duplicates(lists):
    # without_duplicates = list()
    # for i in lists:
    #     if i not in without_duplicates:
    #         without_duplicates.append(i)
    # return without_duplicates
    return list(set(lists))

def run() -> None:
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()