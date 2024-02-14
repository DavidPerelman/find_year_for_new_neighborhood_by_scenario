import pandas as pd
from create_scenario_by_first_year import create_scenario_by_first_year
from filter_2020_none import filter_2020_none
from merge_all_data import merge_all_data
from filter_2020_was_built import filter_2020_was_built
from sum_scnarios_was_built import sum_scnarios_was_built
from split_final_table import split_final_table
from melt_was_built_by_years import melt_was_built_by_years
from sort_was_built_by_jump_percent import sort_was_built_by_jump_percent

pd.set_option('display.max_columns', 500)

#העלת משתנים להרצת הקוד
df_inputs_outputs = pd.read_excel('inputs_outputs.xlsx')

software_path=df_inputs_outputs['location'][0]

scenarios = ['housing_scenario', 'jtmt_scenario', 'trend_scenario']

filter_2020_none_tables = []

# סינון טבלאות שלא בנו בהן ב-2020
for scenario in scenarios:
    filter_2020_none_tables.append(filter_2020_none(software_path, scenario))

filter_2020_was_built_tables = []

# סינון טבלאות שבנו בהן ב-2020
for scenario in scenarios:
    filter_2020_was_built_tables.append(filter_2020_was_built(software_path, scenario))

scenarios_by_first_year = []

for table in filter_2020_none_tables:
    scenarios_by_first_year.append(create_scenario_by_first_year(table))

# טבלה באיזה שנה התחילו לבנות בכל תרחיש
find_year_for_new_neighborhood_by_scenario = merge_all_data(scenarios_by_first_year)

# פיצול לשנים אחידות ולא אחידות שהתחילו לבנות בהן לפי התרחישים
split_final_table(software_path, find_year_for_new_neighborhood_by_scenario)

# חישוב תוספת בניה ואחוז גדילה בשכונות שבנו בהן ב-2020
filtered_2020_was_built_tables = sum_scnarios_was_built(filter_2020_was_built_tables)

# איחוד בכל תרחיש לפי אחוז גדילה מחולק לפי שנים
melted_was_built_by_years = melt_was_built_by_years(filtered_2020_was_built_tables)    

# איחוד כל התרחישים ומיון לפי אחוז גדילה מהקטן לגדול
sort_was_built_by_jump_percent(software_path, melted_was_built_by_years)