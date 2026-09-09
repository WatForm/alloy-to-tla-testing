import config
from controller import *
import os
import json


def check_SAT_UNSAT(analyzer, apalache):
	
	analyzer_SAT = "Solution index" in analyzer

	if analyzer_SAT and "Invariant _command" in apalache and "violated" in apalache:
		return (True, "SAT")
	elif (not analyzer_SAT) and "No error" in apalache:
		return (True, "UNSAT")

	return (False, "unexpected outcome")


def test_translate_run_and_time_tla(model_name):

	tla_path = model_name.replace(".als",".tla")

	translation_response = run_command(f"{config.dashplus} -tla {model_name}")

	if not translation_response.ok():
		test_fail(model_name,compose_message(translation_response))
		return (0,1)

	apalache_run_response = run_command(f"{config.apalache} {tla_path}")
	if not apalache_run_response.ok():
		if apalache_run_response.return_code == 1 and apalache_run_response.stderr == "":
			test_fail(model_name,compose_message(apalache_run_response))
			return (0,1)

	analyzer_run_response = run_command(f"{config.alloy} {model_name}")
	if not analyzer_run_response.ok():
		test_fail(model_name,compose_message(analyzer_run_response))
		return (0,1)

	apalache_output = apalache_run_response.stdout + "\n" + apalache_run_response.stderr
	(correct, msg) = check_SAT_UNSAT(analyzer_run_response.stdout, apalache_output)

	final_result = f"""
Analyzer time: {analyzer_run_response.time}
TLC run time: {apalache_run_response.time}
Translation and Run time: {apalache_run_response.time + translation_response.time}
		"""
	
	if correct:
		test_pass(model_name, final_result)
		return (1,0)
	else:
		test_fail(model_name, f"possibly incorrect SAT/UNSAT")
		return (0,1)


	test_fail(model_name, "something went wrong")
	return (0,1)
	


if __name__ == "__main__":
    controller(test_translate_run_and_time_tla) 