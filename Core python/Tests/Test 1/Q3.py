
def convertToMeter(dist):
    return dist * 1000

dist = int(input('Enter the distance in km: '))
meter = convertToMeter(dist)
centi = meter * 100

print(f'The {dist} km in meter is: {meter}')
print(f'The {dist} km in centimeter is: {centi}')