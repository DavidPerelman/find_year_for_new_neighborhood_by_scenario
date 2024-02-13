import pandas as pd
from create_scenario_by_first_year import create_scenario_by_first_year
from filter_2020_none import filter_2020_none
from merge_all_data import merge_all_data
from filter_2020_was_built import filter_2020_was_built
from sum_scnarios_was_built import sum_scnarios_was_built
from split_final_table import split_final_table

#העלת משתנים להרצת הקוד
df_inputs_outputs = pd.read_excel('inputs_outputs.xlsx')

software_path=df_inputs_outputs['location'][0]

scenarios = ['housing_scenario', 'jtmt_scenario', 'trend_scenario']

# for scenario in scenarios:
#     filter_2020_none(software_path, scenario)

# for scenario in scenarios:
#     filter_2020_was_built(software_path, scenario)

# for scenario in scenarios:
#     create_scenario_by_first_year(software_path, scenario)

# merge_all_data(software_path)

# split_final_table(software_path)

sum_scnarios_was_built(software_path, 'jtmt_scenario')
for scenario in scenarios:
    sum_scnarios_was_built(software_path, scenario)
