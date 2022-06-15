from os.path import dirname, abspath, join

if __name__ == "__main__":
    
    ROOTPATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    WEEK2PATH = join(ROOTPATH, "week_2")
    DAY2PATH = join(WEEK2PATH, "day_2")
    DATAPATH = join(DAY2PATH, "data")
    FAKENAMES = join(DATAPATH, "fake_names_list.txt")
    print(FAKENAMES)
    file = open(FAKENAMES, 'r')

    lines = file.readlines()
    nameslist = [i.split(';')[1] for i in lines]
    print(nameslist)
    # for i in lines:
    #     print(i.split(';')[1])