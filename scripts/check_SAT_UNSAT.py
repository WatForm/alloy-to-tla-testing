
import config
from single_threaded_controller import *
import os

import json
import re


controller = Controller(".als",["./models/simple-models"])



def check_SAT_UNSAT(path_name):

	receipt_file = f"{path_name}"+".json"
	out_file = f"{path_name}".replace(".als",".tla") + ".out"


	instance_exists = -1
	instance_detected = -1

	with open(receipt_file) as rf:
		receipt = json.load(rf)
		main_command = [k for k in receipt["commands"].keys()][0]
		instance_exists = 1 if "solution" in receipt["commands"][main_command] else 0

		
		with open(out_file) as of:
			contents = of.read()
			if "Invariant _command is violated by the initial state:" in contents:
				instance_detected = 1
			elif "Model checking completed. No error has been found." in contents:
				instance_detected = 0

	AA_msg = "❌"
	if instance_exists == 1:
		AA_msg = "✅ I"
	elif instance_exists == 0:
		AA_msg = "✅ No I"

	TLC_msg = "❌"
	if instance_detected == 1:
		TLC_msg = "✅ I"
	elif instance_detected == 0:
		TLC_msg = "✅ No I"

	result = "pass" if instance_detected != -1 and instance_exists == instance_detected else "fail"

	print(AA_msg+"\t\t"+TLC_msg+"\t\t"+result+" - "+path_name)

	
	
	

	
	






    

if __name__ == "__main__":

	print("Checking the SAT/UNSAT output of the default commands of .als files, compared to the output of tlc")

	print("✅ - output is one of the expected possible outputs")
	print("❌ - output is unexpected, the file needs to be examined")
	print("I - instance exists")
	print("no I - no instance exists")


	print("Alloy\t\tTLC\t\tresult")
    
	path_dict = controller.get_paths()

	for source in path_dict:
		files = path_dict[source]
		for f in files:
			check_SAT_UNSAT(f)