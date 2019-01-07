#! /usr/bin/python
import random;
import matplotlib.pyplot as plt;
import numpy as np;

class Beutel:
    def __init__(self):
        self.ones = 2;
        self.origones = 2;
        self.knallerbse3 = 1;
        self.knallerbse2 = 2;
        self.knallerbse1 = 4;
        self.nrchips = self.ones + self.knallerbse3 + self.knallerbse2 + self.knallerbse1;
    
    def nextround(self):
        self.origones += 2;
        self.ones = self.origones;
        self.knallerbse3 = 1;
        self.knallerbse2 = 2;
        self.knallerbse1 = 4;
        self.nrchips = self.ones + self.knallerbse3 + self.knallerbse2 + self.knallerbse1;
    
    def draw(self):
        """The sign of the integer encodes wether it is a one (positive) or a knallerbse (negative)"""
        mynr = random.randint(0, self.nrchips - 1);
        self.nrchips -= 1;
        if mynr < self.ones:
            self.ones -= 1;
            return 1;
        if mynr < self.ones + self.knallerbse1:
            self.knallerbse1 -= 1;
            return -1;
        if mynr < self.ones + self.knallerbse1 + self.knallerbse2:
            self.knallerbse2 -= 1;
            return -2;
        else:
            self.knallerbse3 -= 1;
            return -3;

class Trank:
    def __init__(self):
        self.length = 0;
        self.knallerbsen = 0;

timeseries = []
experiments = 20000;
for j in range(experiments):
    beutel = Beutel();
    tranklens = [];
    for i in range(5):
        trank = Trank();
        while trank.knallerbsen <= 7:
            chip = beutel.draw();
            if chip > 0:
                trank.length += chip;
            else:
                trank.length += (-chip);
                if trank.knallerbsen - chip > 7:
                    tranklens.append(trank.length)
                trank.knallerbsen += (-chip);
        beutel.nextround()
#    print(tranklens);
    timeseries.append(tranklens)
for j in range(5):
    dataset = [timeseries[i][j] for i in range(experiments)];
    print ("Round %i: mittlere Trank Laenge = %f, Width of distribution: %f"%(j, np.mean(dataset), np.var(dataset)))
    mybins = [min(dataset) - 0.5, min(dataset) + 0.5];
    while mybins[-1] < max(dataset):
        mybins.append(mybins[-1] + 1);
    plt.hist(dataset, bins=mybins)
    plt.savefig("fig%i.png"%(j))
    plt.close()
