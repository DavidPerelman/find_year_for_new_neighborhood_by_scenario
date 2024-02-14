import pandas as pd

def sort_was_built_by_jump_percent(software_path, melted_was_built_by_years):

    frames = [melted_was_built_by_years[0], melted_was_built_by_years[1], melted_was_built_by_years[2]]

    result = pd.concat(frames)

    result = result.sort_values('jump_percent', ascending=False)

    result.to_excel(r'{}\final\table_sort_was_built_by_jump_percent.xlsx'.format(software_path), index=False)
