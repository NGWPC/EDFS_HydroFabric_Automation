import pytest
import os
from ..utils import compare_images_util

def test_EDS_Svs_CASE_7_subcase3(test_name,load_scenario_data,scenarios,fetch_docker_details,run_docker_script,fetch_notebook_location_details,fetch_table_details):
    tn = test_name + '.json'
    folder_name = 'PI7/data'

    docker_commands,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    for docker_command in docker_commands:
         run_docker_script(folder_name,tn,scenarios,docker_command)
         print("The command ran successfully.")
    input_notebook_location, output_notebook_location = fetch_notebook_location_details(folder_name,tn,scenarios)
    expected_fields = fetch_table_details(folder_name,tn,scenarios)
    print(input_notebook_location)
    print(output_notebook_location)
#     compare_images_util.verify_gdf_output(os.path.expanduser(output_notebook_location),tag_name = 'compare_image')
    compare_images_util.image_differences(input_notebook_location,os.path.expanduser(output_notebook_location))
    compare_images_util.verify_table_fields(os.path.expanduser(output_notebook_location),expected_fields,tag_name = 'table_validation')