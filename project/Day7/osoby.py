db= []

with open('osoby.csv') as file:
    file.readline() #pomija wiersz

    for line in file:
        line = line.strip() #usuwanie whitespace
        data = line.split(',') #tworzy liste
        data[0] = int(data[0]) #zmieniamy na int
        data[3] = int(data[3])
        db.append(data)

db.append([6,'Ewa', 'Pilot', '37'])

for person in db:
    print(person)

with open ('osoby.csv', 'r+') as file:

    data_to_write = []

    for person_data in db:
        person_data[0] = str(person_data[0])
        person_data[3] = str(person_data[3]) #zminiamy int na str
        line = ','.join(person_data) #tworzy liste z slow z przecinkiem pomiedzy
        line = line + '\n' #dodajemy enter na koncu
        data_to_write.append(line) #dodajemy cos na koniec

    file.writelines(data_to_write) #zapisujemy do pliku

