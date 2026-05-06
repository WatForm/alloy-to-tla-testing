


import config
from controller import *
import os

def test_alloy_model_to_tla_model_is_translateable(path_name):


    cmd = f"{config.dashplus} -tla {path_name}"

    (output,err,rc, time_taken) = run_command(cmd)
    print(output)
    

if __name__ == "__main__":
    controller(test_alloy_model_to_tla_model_is_translateable) 