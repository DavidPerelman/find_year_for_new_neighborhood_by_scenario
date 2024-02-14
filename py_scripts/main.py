import pandas as pd
from create_scenario_by_first_year import create_scenario_by_first_year
from filter_2020_none import filter_2020_none
from merge_all_data import merge_all_data
from filter_2020_was_built import filter_2020_was_built
from sum_scnarios_was_built import sum_scnarios_was_built
from split_final_table import split_final_table
from melt_was_built_by_years import melt_was_built_by_years
from sort_was_built_by_jump_percent import sort_was_built_by_jump_percent

#העלת משתנים להרצת הקוד
df_inputs_outputs = pd.read_excel('inputs_outputs.xlsx')

software_path=df_inputs_outputs['location'][0]

scenarios = ['housing_scenario', 'jtmt_scenario', 'trend_scenario']

# סינון טבלאות שלא בנו בהן ב-2020
for scenario in scenarios:
    filter_2020_none(software_path, scenario)

# סינון טבלאות שבנו בהן ב-2020
for scenario in scenarios:
    filter_2020_was_built(software_path, scenario)

for scenario in scenarios:
    create_scenario_by_first_year(software_path, scenario)

# טבלה באיזה שנה התחילו לבנות בכל תרחיש
merge_all_data(software_path)

# פיצול לשנים אחידות ולא אחידות שהתחילו לבנות בהן לפי התרחישים
split_final_table(software_path)

# חישוב תוספת בניה ואחוז גדילה בשכונות שבנו בהן ב-2020
for scenario in scenarios:
    sum_scnarios_was_built(software_path, scenario)

# איחוד בכל תרחיש לפי אחוז גדילה מחולק לפי שנים
for scenario in scenarios:
    melt_was_built_by_years(software_path, scenario)

# איחוד כל התרחישים ומיון לפי אחוז גדילה מהקטן לגדול
sort_was_built_by_jump_percent(software_path)