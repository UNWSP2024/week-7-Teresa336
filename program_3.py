# Programmer: Teresa Fischer
# Date: 10/15/24
# Program #3: US_Population

def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.
    list_of_lists = []
    data = 0
    while True:
        data = [int(input("Enter the year:")), input("Enter the state:"), int(input("Enter the population:"))]
        list_of_lists.append(data)
        user_input = input('Do you want to enter another set of data? (Y/N)')
        if user_input == 'Y':
            continue
        else:
            break
    # Store all of this information in a list of lists.  For example it might be stored like this:
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    print(list_of_lists)
    # Now have the user enter a year.
    year = int(input("Enter a year for total population:"))
    
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    sum_population_for_year(list_of_lists, year)



def sum_population_for_year(all_entered_values, year_to_sum):
    # Loop through and sum the populations for the appropriate year.
    total_population = 0
    for item in all_entered_values:
        if item[0] == year_to_sum:
            total_population += item[2]

    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.

    # print the totalled population
    print('The total population for', year_to_sum, 'is:', total_population, 'people')

# Call the main function.
if __name__ == '__main__':
    main()

