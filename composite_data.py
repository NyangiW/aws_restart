import csv
import copy
#defining a dictionary that will sercve as a composite type for reading tabular data
myVehicle =  {"Vin" : "<empty>", "make" : "<empty>", "model" : "<empty>", "year": 0, "range" : 0, "topspeed" : 0, "zerosixty" : 0.0, "mileage" : 0}
for key, value in myVehicle. items():
    print ("{}:{}" .format(key,value))
#define an empty list that will hold the car inventory to be read
myInventoryList = []
#copying a csv file into the momory
#a with open syntaxx statement will be introduced
with open ('car_fleet.csv')  as csvFile:
    csvReader = csv.reader (csvFile, delimiter = ',')
    linecount=0
    for row in csvReader:
        if linecount == 0:
            print(f'Column names are: {", ".join(row)}')  
            linecount += 1
    else : 
         print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
         currentVehicle = copy.deepcopy(myVehicle)  
         currentVehicle["vin"] = row[0]  
         currentVehicle["make"] = row[1]  
         currentVehicle["model"] = row[2]  
         currentVehicle["year"] = row[3]  
         currentVehicle["range"] = row[4]  
         currentVehicle["topSpeed"] = row[5]  
         currentVehicle["zeroSixty"] = row[6]  
         currentVehicle["mileage"] = row[7]  
         myInventoryList.append(currentVehicle)  
         linecount += 1  
    print(f'Processed {lineCount} lines.')
    currentVehicle == copy.deepcopy(myVehicle)
    # By default, python does shallow copy of complex data type. A shallow copy referes to the storsge location of myVehicle dictionary varriable
    # The above line makes sure that new storage bxes are created in memory to store a new tabular data that is being created 
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print ("{}: {}" .format(key,value))
            print ("-----")