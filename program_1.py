# Programmer: Teresa Fischer
# Date: 10/15/24
# Program #1: Rainfall

# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.


def rainfall_program():
    # Get rainfall input and add to list
    rainfall = []
    print('Give the rainfall for each month in inches')
    rainfall.append(int(input('Enter the rainfall for January:')))
    rainfall.append(int(input('Enter the rainfall for February:')))
    rainfall.append(int(input('Enter the rainfall for March:')))
    rainfall.append(int(input('Enter the rainfall for April:')))
    rainfall.append(int(input('Enter the rainfall for May:')))
    rainfall.append(int(input('Enter the rainfall for June:')))
    rainfall.append(int(input('Enter the rainfall for July:')))
    rainfall.append(int(input('Enter the rainfall for August:')))
    rainfall.append(int(input('Enter the rainfall for September:')))
    rainfall.append(int(input('Enter the rainfall for October:')))
    rainfall.append(int(input('Enter the rainfall for November:')))
    rainfall.append(int(input('Enter the rainfall for December:')))

    # Calculate total rainfall, average monthly rainfall, and months with highest and lowest ammounts
    total_rainfall = sum(rainfall)
    average_monthly_rainfall = (total_rainfall / 12)

    # Find th highest and lowest month index
    highest_month_index = rainfall.index(max(rainfall))
    lowest_month_index = rainfall.index(min(rainfall))


    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    # Find th highest and lowest month from index
    highest_month = months[highest_month_index]
    lowest_month = months[lowest_month_index]

    # Display calculations
    print('Total rainfall for the year:', total_rainfall, 'inches')
    print('Average monthly rainfall:', average_monthly_rainfall, 'inches')
    print('Month with highest rainfall:', highest_month)
    print('Month with lowest rainfall:', lowest_month)

rainfall_program()
