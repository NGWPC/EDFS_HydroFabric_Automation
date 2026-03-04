import pytest
from ..helpers import validate_directories_files

def test_EDS_Svs_CASE_7_subcase4(test_name,load_scenario_data,scenarios,fetch_docker_details,run_docker_script):
    tn = test_name + '.json'
    folder_name = 'PI7/data'

    docker_commands,dir_paths = fetch_docker_details(folder_name,tn,scenarios)
    for docker_command in docker_commands:
         run_docker_script(folder_name,tn,scenarios,docker_command)
         print("The command ran successfully.")
    directory_locations,directory_contents,flag = load_scenario_data(folder_name,tn,scenarios)
    validate_directories_files(directory_locations,directory_contents,flag)