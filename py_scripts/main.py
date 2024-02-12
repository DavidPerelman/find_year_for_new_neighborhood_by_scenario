import pandas as pd
from create_scenario_by_first_year import create_scenario_by_first_year
from filter_2020_none import filter_2020_none
from merge_all_data import merge_all_data
from split_final_table import split_final_table

# scenarios = ['housing_scenario', 'jtmt_scenario', 'trend_scenario']

# for scenario in scenarios:
#     filter_2020_none(scenario)

# for scenario in scenarios:
#     create_scenario_by_first_year(scenario)

# merge_all_data()

split_final_table()