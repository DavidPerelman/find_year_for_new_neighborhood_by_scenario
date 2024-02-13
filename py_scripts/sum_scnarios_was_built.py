import pandas as pd

pd.set_option('display.max_columns', 500)

def sum_scnarios_was_built(software_path, scenario):
    filtered_2020_was_built = pd.read_excel(r'{}\filter_2020_was_built_scenarios\filter_2020_was_built_{}.xlsx'.format(software_path, scenario))

    # column_pairs = [('hh_total', 'add_aprt_2020_2025')]
    # Create a DataFrame object
    print(filtered_2020_was_built['hh_total'] + filtered_2020_was_built['add_aprt_2020_2025'])
    # filtered_2020_was_built['hh_total'] + filtered_2020_was_built['add_aprt_2020_2025']
    # print(column_pairs)


   # Iterate through each row in the DataFrame
    for index, row in filtered_2020_was_built.iterrows():
        Taz_num = row[0]
        # print('Taz_num: ', Taz_num)
        # Initialize a flag to track if all elements in the row are equal
        sum_each_tuz = 0
         # Iterate through each element in the row starting from the second element
        for i in range(2, len(row)):
            sum_each_tuz += row[i - 1]
            # print(row)
            filtered_2020_was_built['new'] = sum_each_tuz
            # Check if the current element is equal to the previous element
        
        # Print the result for the current row

    # new_equal = pd.DataFrame(sum_scnarios_was_built_new_table)
    print(filtered_2020_was_built)
    # new_equal.to_excel(r'{}\final\new_neighborhood_by_year_for_all_scenarios.xlsx'.format(software_path), index=False)
