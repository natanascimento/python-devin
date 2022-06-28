from os.path import abspath, dirname, join


def reader_with_list(path:str):
  lines = []
  
  with open(path) as file:
    lines = file.readlines()
  
  for line in lines:
    print(line)
  
  
def reader_with_dictionary(path:str):
  info = {"id": "",
          "name": "",
          "country": ""}
  
  with open(path) as file:
    lines = file.readlines()
  
  for line in lines:
      line = line.split(";")
      info["id"] = line[0]
      info["name"] = line[1]
      info["country"] = line[2]
  
      print(info)

def reader_with_list_comp(path:str):
  lines = [name.split(";")[1] for name in open(path).readlines()]
  print(lines)

def main():
  ROOT_PATH = dirname(dirname(abspath(__file__)))
  DATA_PATH = join(ROOT_PATH, "data")
  FAKE_FILE_PATH = join(DATA_PATH, "fake_names_list.txt")
  reader_with_list_comp(FAKE_FILE_PATH)