import sys

def temperatures(temperature):
    max_temp = max(temperature)
    min_temp = min(temperature)
    mean_temp = sum(temperature) / len(temperature)
    
    return max_temp, min_temp, mean_temp

def check_temperature():
    if len(sys.argv) < 2:
        print("No temperature readings provided.")
    else:
        temp_readings = []  # Changed the variable name here to avoid conflict

        for i in range(1, len(sys.argv)):
            temp_readings.append(float(sys.argv[i]))

        max_temperature, min_temperature, mean_temperature = temperatures(temp_readings)

        print(f"Maximum temperature: {max_temperature}")
        print(f"Minimum temperature: {min_temperature}")
        print(f"Mean temperature: {mean_temperature}")

check_temperature()
