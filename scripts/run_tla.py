
import config
from single_threaded_controller import *
import os


controller = Controller(".tla",["./models/simple-models"])

def run_tla(path_name):

    cmd = f"{config.tlc} {path_name} > {path_name}.out"

    result = controller.run_command(cmd)

    passed = True
    message = "Success"

    
    if result.timeout:
        message = "Timeout"

    print(("✅" if passed else "❌") + " " + message + "\t" + path_name)

    if not passed and not result.timeout:
        print("unexpected output by tlc, check "+path_name.replace(".tla",".out")+" for details")

    

if __name__ == "__main__":

    print("Key:\n✅ - run without timeout\n❌ - timed out\n")
    
    path_dict = controller.get_paths()

    for source in path_dict:
        files = path_dict[source]
        for f in files:
            run_tla(f)