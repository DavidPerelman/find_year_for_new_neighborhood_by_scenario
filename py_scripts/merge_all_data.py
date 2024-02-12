import pandas as pd

def merge_all_data():
    housing_scenario = pd.read_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\scenarios_by_first_year\scenario_by_first_year_housing_scenario.xlsx')
    jtmt_scenario = pd.read_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\scenarios_by_first_year\scenario_by_first_year_jtmt_scenario.xlsx')
    trend_scenario = pd.read_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\scenarios_by_first_year\scenario_by_first_year_trend_scenario.xlsx')

    housing_scenario.merge(jtmt_scenario, how="outer").fillna(0).merge(trend_scenario, how="outer").fillna(0).to_excel(r'C:\Users\dpere\Documents\JTMT\find_year_for_new_neighborhood_by_scenario\find_year_for_new_neighborhood_by_scenario.xlsx', index=False)