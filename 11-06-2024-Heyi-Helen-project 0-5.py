#carfinder
AllowedVehiclesList= (
    "Ford F-150",
    "Chevrolet Silverado", 
    "Tesla CynerTruck",
    "Toyota Tundra",
    "Nissan Titan",
    "Rivian R1T",
    "Ram 1500"
)
AuthorizedVehicles=AllowedVehiclesList
print("*********************")
print("Autocountry vehicle finder v0.1")
print("*********************")
print("please enter the following number below from the following menu:")
print("1. PRINT all authorized vehicles")
print("2. SEARCH for authorized vehicle")
print("3. ADD authorized Vehicle")
print("4. DELETE Authorized Vehicle")
print("5. Exit")
print("*********************")
option= '5'
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
elif option== '3':
    print("Please enter the full vehicle name you would like to add:")
    vehicle_Name= input()
    if vehicle_Name not in AuthorizedVehicles:
        print(f'You have added "{vehicle_Name}" as an authorized vehicle')
        
elif option== '4':
    print("Please enter the full vehicle name you would like to REMOVE:")
    vehicle_Name= input()
    if vehicle_Name in AuthorizedVehicles:
        print(f'Are you sure you want to remove "{vehicle_Name}" from the authorized vehicles list?')
    else:
        print(f'Are you sure you want to remove"{vehicle_Name}" from the authorized vehicles list?')
answer=input()
if answer== 'yes':
    print(f'You have REMOVED "{vehicle_Name}" as an authorized vehicle')
elif option== '5' :
    print ("Thank you for using the AutoCountry vehicle Finder, good-bye!")
    print("Program closes after keypress")