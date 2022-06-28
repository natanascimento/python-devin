from os.path import dirname, abspath, join

def reader(path:str):
    names = [name.split(";")[2] for name in open(path).readlines()]
    return names

if __name__ == "__main__":
    ROOT_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    WEEK2_PATH = join(ROOT_PATH, "week_2")
    DAY2_PATH = join(WEEK2_PATH, "day_2")
    DAY2_DATA_PATH = join(DAY2_PATH, "data")
    FAKE_DATA_PATH = join(DAY2_DATA_PATH, "fake_names_list.txt")
    # print(ROOT_PATH)
    # print(WEEK2_PATH)
    # print(DAY2_PATH)
    # print(DAY2_DATA_PATH)
    # print(FAKE_DATA_PATH)
    # print()
    # teste = open(FAKE_DATA_PATH).readlines()
    # print(teste)  
    print(__name__)
