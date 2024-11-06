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
print("2. Exit")
option= ''
if option== '1' :
    print ("The autoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AuthorizedVehicles: 
        print(vehicle)
elif option== '2' :
    print ("Thank you for using the AutoCountry vehicle Finder, good-bye!")
    print("Program closes after keypress")

    

