
import config
from single_threaded_controller import *
import os


controller = Controller(".als",["./models/simple-models"])

def run_tla(path_name):

    cmd = f"{config.alloy} {path_name}"

    controller.run_command(cmd)

    cmd = f"cp ./libs/alloy/receipt.json {path_name}.json"

    controller.run_command(cmd)



    

if __name__ == "__main__":
    
    path_dict = controller.get_paths()

    for source in path_dict:
        files = path_dict[source]
        for f in files:
            run_tla(f)