f = open("week_2/day_2/data/fake_names_list.txt")
print(f.read())

y = [x.split(";")[1] for x in f] # uma forma de ver só pelo nome
# y = [x for x in f]

print(y)
