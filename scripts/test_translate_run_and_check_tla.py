import config
from controller import *
import os
import json


def check_SAT_UNSAT(analyzer, tlc):

	if "commands" not in analyzer:
		return (False, "unexpected receipt.json file structure"+str(analyzer))
	keys = list(analyzer["commands"].keys())
	if len(keys) == 0:
		return (False, "unexpected receipt.json file structure"+str(analyzer))
	
	analyzer_SAT = "solution" in analyzer["commands"][keys[0]]

	if analyzer_SAT and "Invariant _command is violated by the initial state:" in tlc:
		return (True, "SAT")
	elif (not analyzer_SAT) and "Model checking completed. No error has been found." in tlc:
		return (True, "UNSAT")
	

	return (False, "unexpected outcome")


def test_translate_run_and_time_tla(model_name):


	tla_path = model_name.replace(".als",".tla")

	cmd = f"{config.dashplus} -tla {model_name}"

	time = 0 # this is meant to measure translation time + running time
	(output,err,rc,time_taken) = run_command(cmd)
	time += time_taken

	if rc != 0:
		common_err_response(cmd, output, err, time)
		return (0,1)

	cmd = f"{config.tlc} {tla_path}"
	(output,err,rc,time_taken) = run_command(cmd)
	time+=time_taken

	if err in ["Timeout", "Exception"]:
		common_err_response(cmd, output, err, time)
		return (0,1)

	tla_output = output + "\n" + err

	cmd = f"{config.alloy} {model_name}"
	(output,err,rc,time_taken) = run_command(cmd)
	time_taken_alloy = time_taken

	if rc != 0:
		common_err_response(cmd, output, err, time)
		return (0,1)

	try:
		with open("./libs/alloy/receipt.json") as f:
			analyzer_contents = json.load(f)
			(correct, msg) = check_SAT_UNSAT(analyzer_contents, tla_output)
			if correct:
				common_pass_response(f"SAT/UNSAT correctness check {model_name}",msg,"",time)
				return (1,0)
			else:
				common_err_response(f"SAT/UNSAT correctness check {model_name}","",msg,time)
				return (0,1)
	except Exception as error:
		common_err_response("reading receipt","",str(error),time)
		return (0,1)

	common_err_response("", "", "something went wrong", time)
	return (0,1)


if __name__ == "__main__":
    controller(test_translate_run_and_time_tla) 