
import config
from single_threaded_controller import *
import os


controller = Controller(".als",["./models/simple-models"])

tmp_file = "./libs/alloy/receipt.json"

def run_tla(path_name):

    cmd = f"{config.alloy} {path_name}"

    controller.run_command(cmd)

    cmd = f"cp {tmp_file} {path_name}.json"

    controller.run_command(cmd)

    print("ran the Alloy Analyzer on "+path_name)


    

if __name__ == "__main__":
    
    path_dict = controller.get_paths()

    for source in path_dict:
        files = path_dict[source]
        for f in files:
            run_tla(f)