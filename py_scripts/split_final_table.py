import pandas as pd

def split_final_table():
    find_year_for_new_neighborhood_by_scenario = pd.read_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\find_year_for_new_neighborhood_by_scenario.xlsx')

    equal_data = []
    not_equal_data = []

   # Iterate through each row in the DataFrame
    for index, row in find_year_for_new_neighborhood_by_scenario.iterrows():
        Taz_num = row[0]

        # Initialize a flag to track if all elements in the row are equal
        all_equal = True

         # Iterate through each element in the row starting from the second element
        for i in range(2, len(row)):
            # Check if the current element is equal to the previous element
            if row[i] != row[i - 1]:
                all_equal = False
                break
        
        # Print the result for the current row
        if all_equal:
            data_row = {'Taz_num': Taz_num, 'year': row[2]}
            equal_data.append(data_row)
        else:
            # data_row = {'Taz_num': Taz_num, 'year': row[2]}
            not_equal_data.append(row)

    new_equal = pd.DataFrame(equal_data)
    new_not_equal = pd.DataFrame(not_equal_data)
    new_equal.to_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\final\new_neighborhood_by_year_for_all_scenarios.xlsx', index=False)
    new_not_equal.to_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\final\new_neighborhood_by_years_by_scenarios.xlsx', index=False)
