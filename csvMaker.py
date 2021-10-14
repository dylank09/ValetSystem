import csv  

#name, GPSLocation, storeManager, rating, status, valets
data = ['name', 'GPSLocation', 'rating', 'status', 'valets']
with open('stores.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the data
    writer.writerow(data)

    f.close()