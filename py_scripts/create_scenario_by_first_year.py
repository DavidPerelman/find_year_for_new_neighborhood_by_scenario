import pandas as pd

def create_scenario_by_first_year(excel_scenario):
    data = []

    # Iterate through each row in the DataFrame
    for index, row in excel_scenario.iterrows():
        first_positive = None
        column_name = None
        Taz_num = row[0]
        scenario = row[7]
        
        # Iterate through each element in the row
        for column, value in row[1:].items():
            column_value = row[column]
            if pd.notna(column_value) and column_value > 0:
                first_positive = column_value
                column_name = column
                break
        if first_positive is not None:
            data_row = {'Taz_num': Taz_num, scenario: column_name[9:13]}
            data.append(data_row)
        else:
            print(f"No positive numbers found for row {index}")

    new_df = pd.DataFrame(data)
    return new_df
