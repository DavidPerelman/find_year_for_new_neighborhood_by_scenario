import pandas as pd

def melt_was_built_by_years(filtered_2020_was_built_tables):
    melted_was_built_by_years = []

    for filtered_2020_was_built_table in filtered_2020_was_built_tables:
        table_scenario = pd.DataFrame(filtered_2020_was_built_table).melt(id_vars='Taz_num', value_vars=['jump_percent_2020_2025','jump_percent_2025_2030', 'jump_percent_2030_2035',
                                                                        'jump_percent_2035_2040', 'jump_percent_2040_2045', 'jump_percent_2045_2050'], 
                                                                        var_name='years', value_name='jump_percent').sort_values('Taz_num')

        table_scenario['scenario'] = filtered_2020_was_built_table['scenario'][0]

        melted_was_built_by_years.append(table_scenario)

    return melted_was_built_by_years