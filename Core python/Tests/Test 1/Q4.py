def calculateCost(area, int_cost, ext_cost):
    return 8 * area * int_cost + 7 * area * ext_cost

area = int(input('Enter the area of one wall: '))
int_cost = int(input('Enter the cost for interior wall: '))
ext_cost = int(input('Enter the cost for exterior wall: '))

total_cost = calculateCost(area, int_cost, ext_cost)

print('The total cost to paint both rooms is:', total_cost)