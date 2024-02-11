import pandas as pd
import os

forecast_2020 = pd.read_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\data\forecast_2020_230720.xlsx')
housing_scenario = pd.read_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\data\230720_kibolt_jew_till_2050_housing_scenario.xlsx')
jtmt_scenario = pd.read_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\data\230720_kibolt_jew_till_2050_jtmt_scenario.xlsx')
trend_scenario = pd.read_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\data\230720_kibolt_jew_till_2050_trend_scenario.xlsx')

def filter_2020_none():
    rslt_df = forecast_2020[forecast_2020['hh_total'] == 0] 

    filtered_table = pd.merge(housing_scenario, rslt_df, how='inner', left_on='Taz_num', right_on='TAZ')

    sliced_df = filtered_table.loc[:, 'Taz_num':'add_aprt_2045_2050']

    sliced_df.to_excel("output.xlsx", index=False)

filter_2020_none()