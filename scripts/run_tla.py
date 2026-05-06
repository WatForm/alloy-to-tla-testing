
import config
from single_threaded_controller import *
import os


controller = Controller(".tla",["./models/simple-models"])

def run_tla(path_name):

    cmd = f"{config.tlc} {path_name}"

    result = controller.run_command(cmd)

    passed = False
    message = "Error"

    if "Model checking completed. No error has been found." in result.output:
        message = "Success"
        passed = True
    if result.timeout:
        message = "Timeout"

    print(("✅" if passed else "❌") + " " + message + "\t" + path_name)
    

if __name__ == "__main__":
    
    path_dict = controller.get_paths()

    for source in path_dict:
        files = path_dict[source]
        for f in files:
            run_tla(f)