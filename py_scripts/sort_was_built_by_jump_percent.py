import pandas as pd

def sort_was_built_by_jump_percent(software_path):
    melt_housing_scenario = pd.read_excel(r'{}\melt\melt_housing_scenario.xlsx'.format(software_path,))
    melt_jtmt_scenario = pd.read_excel(r'{}\melt\melt_jtmt_scenario.xlsx'.format(software_path))
    melt_trend_scenario = pd.read_excel(r'{}\melt\melt_trend_scenario.xlsx'.format(software_path))

    frames = [melt_housing_scenario, melt_jtmt_scenario, melt_trend_scenario]

    result = pd.concat(frames)

    result = result.sort_values('jump_percent', ascending=False)

    result.to_excel(r'{}\final\table_sort_was_built_by_jump_percent.xlsx'.format(software_path), index=False)
