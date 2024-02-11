import pandas as pd

df = pd.read_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\data\output.xlsx')

sliced_df = df.loc[:, 'Taz_num':'add_aprt_2045_2050']

print(sliced_df)

data = []

# Iterate through each row in the DataFrame
for index, row in sliced_df.iterrows():
    first_positive = None
    column_name = None
    Taz_num = row[0]
    
    # Iterate through each element in the row
    for column, value in row[1:].items():
        column_value = row[column]
        if pd.notna(column_value) and column_value > 0:
            first_positive = column_value
            column_name = column
            break
    if first_positive is not None:
        # print(row[0])
        data_row = {'Taz_num': Taz_num, 'housing_scenario': column_name[9:13]}
        data.append(data_row)
        print(f"First positive number for Taz_num {Taz_num}, found in year: {column_name}")
    else:
        print(f"No positive numbers found for row {index}")

df = pd.DataFrame(data)
print(df.to_excel("housing_scenario.xlsx", index=False))