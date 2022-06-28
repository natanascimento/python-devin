from os.path import abspath, dirname, join

from faker import Faker

def generate(path:str, gen_number:int=10):
  faker = Faker()
  file = open(path, "w+")
  file.write(f"id;name;country\n")
  for id in range(gen_number):
    file.write(f"{id};{faker.name()};{faker.country()}\n") 
  file.close()
  return "File was created"
  
def main():
  ROOT_PATH = dirname(dirname(abspath(__file__)))
  DATA_PATH = join(ROOT_PATH, "data")
  FAKE_FILE_PATH = join(DATA_PATH, "fake_names_list.txt")
  print(generate(path=FAKE_FILE_PATH, gen_number=1000))