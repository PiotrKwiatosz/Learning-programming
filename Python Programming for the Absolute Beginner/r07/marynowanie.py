# Zamarynuj to
# Demonstruje marynowanie i odkladanie danych na polke

import pickle, shelve

print("Marynowanie list.")
variety = ["lagodny", "pikantny", "kwaszony"]
shape = ["caly", "krojony", "w plasterkach"]
brand = ["Dawtona", "Klimex", "Vortumus"]

f = open("pikle1.dat", "wb")