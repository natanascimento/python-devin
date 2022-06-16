from os.path import dirname, abspath, join

def namesreader(path:str):
    names = [line.split(';')[1] for line in open(path, 'r').readlines()]
    return names
def infodict(path:str):
    info = [dict(id=line.split(';')[0], name=line.split(';')[1], country=line.split(';')[2].split('\n')[0]) for line in open(path, 'r').readlines()]
    return info

if __name__ == "__main__":
    
    ROOTPATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    WEEK2PATH = join(ROOTPATH, "week_2")
    DAY2PATH = join(WEEK2PATH, "day_2")
    DATAPATH = join(DAY2PATH, "data")
    FAKENAMES = join(DATAPATH, "fake_names_list.txt")
    
    print(namesreader(FAKENAMES))
    print(infodict(FAKENAMES))
    # file = open(FAKENAMES, 'r')
    # lines = file.readlines()
    # nameslist = [i.split(';')[1] for i in lines]
    # print(nameslist)

    # for i in lines:
    #     print(i.split(';')[1])