##P1HW2_Travel_RoarkJaLisa
##TravelingExpenses
##9/11/2022
##CTI110P1HW2 - TravelExpense
##JaLisaRoark
budget = 0
travel_destination = 0
gas = 0
accomodation = 0
food = 0
budget= int(input('Enter budget: '))
travel_destination= input('Enter your travel destination: ')
gas= int(input('Please enter the amount you will spend on gas: '))
accomodation= int(input('Approximately, how much will you need for accomodation/hotel?: '))
food= int(input('Last, how much do you need for food: '))
print("Enter budget: " , budget)
print("Travel_destination: " + travel_destination)
print("Enter gas: " , gas)
print("Enter accomodation: " , accomodation)
print("Enter food: " , food)
print('Expenses: ', budget + gas + accomodation + food)
Expenses = budget + gas + accomodation + food
print('Remaining budget: ', budget - Expenses)
