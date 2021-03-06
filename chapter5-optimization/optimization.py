import time
import random
import math

people = [
          ('Seymour', 'BOS'),
          ('Franny', 'DAL'),
          ('Zooey', 'CAK'),
          ('Walt', 'MIA'),
          ('Buddy', 'ORD'),
          ('Les', 'OMA')
         ]

# LaGuardia airport in New York
destination='LGA'


flights = {}
for line in file('schedule.txt'):

    origin, dest, depart, arrive, price = line.strip().split(',')
    flights.setdefault((origin, dest), [])

    flights[(origin, dest)].append((depart, arrive, int(price)))



def getminutes(t):

    x = time.strptime(t, '%H:%M')
    return x[3] * 60 + x[4]


def printschedule(r):

    for d in range(0, len(r)/2):

        name = people[d][0]
        origin = people[d][1]

        out = flights[(origin, destination)][r[2*d]]
        ret = flights[(destination, origin)][r[2*d+1]]

        print '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name, origin, out[0], out[1], out[2], ret[0], ret[1], ret[2])


s = [1,4,3,2,7,3,6,3,2,4,5,3]
printschedule(s)

