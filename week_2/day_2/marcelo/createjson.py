import json

def infodict(path1:str, path2:str):
    info = [dict(id=line.split(';')[0], name=line.split(';')[1], country=line.split(';')[2].split('\n')[0]) for line in open(path1, 'r').readlines()
    ][1:]
    jsondict = {f'{x+1}':info[x] for x in range(len(info))}
    file = open(f'{path2}/usersdata.txt', 'w')
    file.write(json.dumps(jsondict))
    return file.close()

if __name__ == "__main__":

    from os.path import dirname, abspath, join
    
    ROOTPATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    WEEK2PATH = join(ROOTPATH, "week_2")
    DAY2PATH = join(WEEK2PATH, "day_2")
    DATAPATH = join(DAY2PATH, "data")
    FAKENAMES = join(DATAPATH, "fake_names_list.txt")
    
    infodict(FAKENAMES, DATAPATH)
