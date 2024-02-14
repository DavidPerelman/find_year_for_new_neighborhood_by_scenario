import pandas as pd

def melt_was_built_by_years(software_path, scenario):
    table_scenario = pd.read_excel(r'{}\new_neighborhood_2020_was_built\new_neighborhood_2020_was_built_jump_percent_by_years_{}.xlsx'.format(software_path, scenario))
    
    table_scenario = table_scenario.melt(id_vars='Taz_num', value_vars=['jump_percent_2020_2025','jump_percent_2025_2030', 'jump_percent_2030_2035',
                                                                        'jump_percent_2035_2040', 'jump_percent_2040_2045', 'jump_percent_2045_2050'], 
                                                                        var_name='years', value_name='jump_percent').sort_values('Taz_num')
    
    table_scenario['scenario'] = scenario

    table_scenario.to_excel(r'{}\melt\melt_{}.xlsx'.format(software_path, scenario), index=False)
