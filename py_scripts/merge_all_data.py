import pandas as pd

def merge_all_data(scenarios_by_first_year):
    housing_scenario = pd.DataFrame(scenarios_by_first_year[0])
    jtmt_scenario = pd.DataFrame(scenarios_by_first_year[1])
    trend_scenario = pd.DataFrame(scenarios_by_first_year[2])

    find_year_for_new_neighborhood_by_scenario = housing_scenario.merge(jtmt_scenario, how="outer").fillna(0).merge(trend_scenario, how="outer").fillna(0)
    return find_year_for_new_neighborhood_by_scenario