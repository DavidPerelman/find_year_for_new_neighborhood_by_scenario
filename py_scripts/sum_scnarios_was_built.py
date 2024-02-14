import pandas as pd

pd.set_option('display.max_columns', 500)

def sum_scnarios_was_built(filter_2020_was_built_tables):
    filtered_2020_was_built_tables = []
    for filtered_2020_was_built in filter_2020_was_built_tables:

        filtered_2020_was_built['sum_aprt_2020_2025'] = filtered_2020_was_built['hh_total'] + filtered_2020_was_built['add_aprt_2020_2025']
        filtered_2020_was_built['sum_aprt_2025_2030'] = filtered_2020_was_built['sum_aprt_2020_2025'] + filtered_2020_was_built['add_aprt_2025_2030']
        filtered_2020_was_built['sum_aprt_2030_2035'] = filtered_2020_was_built['sum_aprt_2025_2030'] + filtered_2020_was_built['add_aprt_2030_2035']
        filtered_2020_was_built['sum_aprt_2035_2040'] = filtered_2020_was_built['sum_aprt_2030_2035'] + filtered_2020_was_built['add_aprt_2035_2040']
        filtered_2020_was_built['sum_aprt_2040_2045'] = filtered_2020_was_built['sum_aprt_2035_2040'] + filtered_2020_was_built['add_aprt_2040_2045']
        filtered_2020_was_built['sum_aprt_2045_2050'] = filtered_2020_was_built['sum_aprt_2040_2045'] + filtered_2020_was_built['add_aprt_2045_2050']

        filtered_2020_was_built['jump_percent_2020_2025'] = filtered_2020_was_built['add_aprt_2020_2025'] / filtered_2020_was_built['hh_total'] * 100
        filtered_2020_was_built['jump_percent_2025_2030'] = filtered_2020_was_built['add_aprt_2025_2030'] / filtered_2020_was_built['sum_aprt_2020_2025'] * 100
        filtered_2020_was_built['jump_percent_2030_2035'] = filtered_2020_was_built['add_aprt_2030_2035'] / filtered_2020_was_built['sum_aprt_2025_2030'] * 100
        filtered_2020_was_built['jump_percent_2035_2040'] = filtered_2020_was_built['add_aprt_2035_2040'] / filtered_2020_was_built['sum_aprt_2030_2035'] * 100
        filtered_2020_was_built['jump_percent_2040_2045'] = filtered_2020_was_built['add_aprt_2040_2045'] / filtered_2020_was_built['sum_aprt_2035_2040'] * 100
        filtered_2020_was_built['jump_percent_2045_2050'] = filtered_2020_was_built['add_aprt_2045_2050'] / filtered_2020_was_built['sum_aprt_2040_2045'] * 100

        filtered_2020_was_built = filtered_2020_was_built.drop(['hh_total', 'add_aprt_2020_2025', 'add_aprt_2025_2030', 'add_aprt_2030_2035', 
                            'add_aprt_2035_2040', 'add_aprt_2040_2045', 'add_aprt_2045_2050', 'sum_aprt_2020_2025', 
                            'sum_aprt_2025_2030', 'sum_aprt_2030_2035', 'sum_aprt_2035_2040', 'sum_aprt_2040_2045',
                            'sum_aprt_2045_2050'], axis=1)
                
        filtered_2020_was_built_tables.append(pd.DataFrame(filtered_2020_was_built))
        
    return filtered_2020_was_built_tables
