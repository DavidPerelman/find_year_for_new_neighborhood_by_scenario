import pandas as pd

def merge_all_data(software_path):
    housing_scenario = pd.read_excel(r'{}\scenarios_by_first_year\scenario_by_first_year_housing_scenario.xlsx'.format(software_path))
    jtmt_scenario = pd.read_excel(r'{}\scenarios_by_first_year\scenario_by_first_year_jtmt_scenario.xlsx'.format(software_path))
    trend_scenario = pd.read_excel(r'{}\scenarios_by_first_year\scenario_by_first_year_trend_scenario.xlsx'.format(software_path))

    housing_scenario.merge(jtmt_scenario, how="outer").fillna(0).merge(trend_scenario, how="outer").fillna(0).to_excel(r'{}\scenarios_by_first_year\find_year_for_new_neighborhood_by_scenario.xlsx'.format(software_path), index=False)