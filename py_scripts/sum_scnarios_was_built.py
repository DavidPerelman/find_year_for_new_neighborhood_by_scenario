import pandas as pd

pd.set_option('display.max_columns', 500)

def sum_scnarios_was_built(software_path, scenario):
    filtered_2020_was_built = pd.read_excel(r'{}\filter_2020_was_built_scenarios\filter_2020_was_built_{}.xlsx'.format(software_path, scenario))

    filtered_2020_was_built['sum_aprt_2020_2025'] = filtered_2020_was_built['hh_total'] + filtered_2020_was_built['add_aprt_2020_2025']
    filtered_2020_was_built['sum_aprt_2025_2030'] = filtered_2020_was_built['sum_aprt_2020_2025'] + filtered_2020_was_built['add_aprt_2025_2030']
    filtered_2020_was_built['sum_aprt_2030_2035'] = filtered_2020_was_built['sum_aprt_2025_2030'] + filtered_2020_was_built['add_aprt_2030_2035']
    filtered_2020_was_built['sum_aprt_2035_2040'] = filtered_2020_was_built['sum_aprt_2030_2035'] + filtered_2020_was_built['add_aprt_2035_2040']
    filtered_2020_was_built['sum_aprt_2040_2045'] = filtered_2020_was_built['sum_aprt_2035_2040'] + filtered_2020_was_built['add_aprt_2040_2045']
    filtered_2020_was_built['sum_aprt_2045_2050'] = filtered_2020_was_built['sum_aprt_2040_2045'] + filtered_2020_was_built['add_aprt_2045_2050']

    filtered_2020_was_built['jump_percent_2020_2025'] = filtered_2020_was_built['add_aprt_2020_2025'] / filtered_2020_was_built['hh_total']
    filtered_2020_was_built['jump_percent_2025_2030'] = filtered_2020_was_built['add_aprt_2025_2030'] / filtered_2020_was_built['sum_aprt_2020_2025']
    filtered_2020_was_built['jump_percent_2030_2035'] = filtered_2020_was_built['add_aprt_2030_2035'] / filtered_2020_was_built['sum_aprt_2025_2030']
    filtered_2020_was_built['jump_percent_2035_2040'] = filtered_2020_was_built['add_aprt_2035_2040'] / filtered_2020_was_built['sum_aprt_2030_2035']
    filtered_2020_was_built['jump_percent_2040_2045'] = filtered_2020_was_built['add_aprt_2040_2045'] / filtered_2020_was_built['sum_aprt_2035_2040']
    filtered_2020_was_built['jump_percent_2045_2050'] = filtered_2020_was_built['add_aprt_2045_2050'] / filtered_2020_was_built['sum_aprt_2040_2045']
    filtered_2020_was_built.to_excel(r'{}\final\new_neighborhood_by_year_for_all_scenarios.xlsx'.format(software_path), index=False)
