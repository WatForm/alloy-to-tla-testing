# goal


# make a subshell with access to tlc
# specifiy the location of the translator (latest version)
# alternately, pin it to the github repo in the flake, and make it available in the shell
# by default, the shell in the flake should have access

# run the translator, then run tlc on the translated code with all schemes
# report times in a csv 

import config
from controller import *
import os

def test_alloy_model_to_tla_model_is_translateable(path_name):


    cmd = f"{config.dashplus} -tla {path_name}"

    (output,err,rc, time_taken) = run_command(cmd)
    if rc != 0:
        common_err_response(cmd, output, err, time_taken)
        return (0,1)
    

if __name__ == "__main__":
    controller(test_alloy_model_to_tla_model_is_translateable) 