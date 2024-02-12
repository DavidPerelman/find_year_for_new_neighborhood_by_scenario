import pandas as pd

def filter_2020_was_built(scenario):
    forecast_2020 = pd.read_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\data\forecast_2020_230720.xlsx')

    excel_scenario = pd.read_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\data\230720_kibolt_jew_till_2050_{}.xlsx'.format(scenario))

    rslt_df = forecast_2020[forecast_2020['hh_total'] > 0] 

    filtered_table = pd.merge(excel_scenario, rslt_df, how='inner', left_on='Taz_num', right_on='TAZ')

    cols = ['Taz_num', 'hh_total','add_aprt_2020_2025', 'add_aprt_2025_2030', 'add_aprt_2030_2035',
            'add_aprt_2035_2040', 'add_aprt_2040_2045', 'add_aprt_2045_2050']
    sliced_df = filtered_table[cols]

    sliced_df.to_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\filter_2020_was_built_scenarios\filter_2020_was_built_{}.xlsx'.format(scenario), index=False)
