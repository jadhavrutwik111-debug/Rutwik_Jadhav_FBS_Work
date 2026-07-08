#convert distance given in feet and inches into meter and centimeter
#take inputs for feet and inches
feet = int(input('Enter the distance in feet: '))
inch = int(input('Enter the distance in inches: '))

#convert feet into inches
f_to_in = feet * 12
inch = inch + f_to_in

#convert into meter and centimeter
centi = inch * 2.54
meter = centi / 100

#display result
print(f'After convertion distance meter = {meter} and centimeter = {centi}')