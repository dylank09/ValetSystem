import csv  
from random import seed
from random import random

with open('stores.csv', 'w', newline='') as f:

    writer = csv.writer(f)

    seed(1)
    for i in range(100):
        #name, GPSLocation, storeManager, rating, status, valets
        data = ['Store'+str(i), str(i*4)+','+str(i*9), str(random()*5), 'status', 'valets']
        # write the data
        writer.writerow(data)

    f.close()
    