# Discription: Conerstions for rods inputed by user


rod_in_meters = 5.0292
furlong_in_rods = 40
mile_in_meters = 1609.34
foot_in_meters = 0.3048
avg_walking_speed = 3.1 

user_rod = float(input("Input rods: "))
print("You input", user_rod, "rods. \n")

print("Conversion")
print("Meters:", user_rod*rod_in_meters)
print("Feet:", (user_rod*rod_in_meters)/foot_in_meters)
print("Miles:", (user_rod*rod_in_meters)/mile_in_meters)
print("Furlongs:", user_rod/furlong_in_rods)
print("Minutes to walk", user_rod, "rods:", (((user_rod*rod_in_meters)/mile_in_meters)/avg_walking_speed)*60)

