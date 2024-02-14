import pandas as pd

def filter_2020_none(software_path, scenario):
    forecast_2020 = pd.read_excel(r'{}\data\forecast_2020_230720.xlsx'.format(software_path))

    excel_scenario = pd.read_excel(r'{}\data\230720_kibolt_jew_till_2050_{}.xlsx'.format(software_path, scenario))

    rslt_df = forecast_2020[forecast_2020['hh_total'] == 0] 

    filtered_table = pd.merge(excel_scenario, rslt_df, how='inner', left_on='Taz_num', right_on='TAZ')

    sliced_df = filtered_table.loc[:, 'Taz_num':'add_aprt_2045_2050']

    sliced_df['scenario'] = scenario

    return sliced_df