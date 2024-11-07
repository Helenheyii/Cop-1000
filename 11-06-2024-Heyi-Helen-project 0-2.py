#carfinder
AllowedVehiclesList= (
    "Ford F-150",
    "Chevrolet Silverado", 
    "Tesla CynerTruck",
    "Toyota Tundra",
    "Nissan Titan"
)
AuthorizedVehicles=AllowedVehiclesList
print("*********************")
print("Autocountry vehicle finder v0.1")
print("*********************")
print("please enter the following number below from the following menu:")
print("1. PRINT all authorized vehicles")
print("2. SEARCH for authorized vehicle")
print("3. Exit")
option= '2'
if option== '1' :
    print ("The autoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AuthorizedVehicles: 
        print(vehicle)
elif option== '2':
    print("**********************")
    print("Please Enter the full Vehicle name:")  
    vehicle_Name= input()
    if vehicle_Name in AuthorizedVehicles:
        print(f"{vehicle_Name} is an authorized vehicle")   
    else:
        print(f"{vehicle_Name} is not an authorized vehicle, if you received this in error please check the spelling and try again.")  
elif option== '3' :
    print ("Thank you for using the AutoCountry vehicle Finder, good-bye!")
    print("Program closes after keypress")
    