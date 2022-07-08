from io import StringIO
import os
import pytest
from scripts import data_processor, data_aggregator

@pytest.mark.parametrize("country,stat,expected", [('Andorra', 'Mean', 1641.42),
     ('Andorra', 'Median', 1538.02),
     ('Andorra', 'Median', 1538.02),
     ('Argentina', 'Median', 125.0)])
def test_challengue(process_data, country, stat, expected):
    data = process_data(file_name_or_type="clean_map_final.csv")
    andorran_median_res = data_aggregator.atitude_stat_per_country(data, country, stat)
    output_location = StringIO()
    data_aggregator.csv_writer(andorran_median_res, output_location)

    res = output_location.getvalue().strip('\r\n')
    assert res == f'Country,{stat}\r\n{country},{expected}'
