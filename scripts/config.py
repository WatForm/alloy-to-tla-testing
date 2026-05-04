# config
# modify this file with each person's config for the tests

# defaults
dashplus = "java -ea -jar ./dashplus/app/build/libs/watform-dashplus.jar"

# table gives output if sat; no output if not sat
alloy = "alloy6"

tlc = "tlc"

sources = [
			'../models/',
			'./models/'
			]
verbose = True
stop_on_first_fail = True
timeout = 30000 # ms
method = "traces"
num_threads = 12  # Number of threads to use for running tests concurrently

def setup(who):
	global dashplus
	global alloy
	global sources 
	global verbose
	global stop_on_first_fail
	global timeout
	global method
	global num_threads
	if who == "nad":
		print("Nancy's settings")
		# don't bother with setup each time; just run from sister directory
		dashplus = "java -ea -jar ../../dashplus/app/build/libs/watform-dashplus.jar "
		sources = [
			#'../models/case-studies/2019-dash-website/bit-counter/',
			#'../models/case-studies/2019-dash-website', 
			#'../models/case-studies/2022-bandali-thesis', 
			#'../models/case-studies/2022-tamjid-thesis',
			#'../models/case-studies/2023-bandali-day-paper',
			'../models/testing',
			]
		verbose = False
		stop_on_first_fail = False
		timeout = 30000 # ms
		method = "traces"
		# set this to 1 if want to see command/output matched up well console output
		num_threads = 1 
		# a good combination when debugging is verbose=False, stop_on_first_fail=True, num_threads=12
	elif who == "mkj":
		# Mathew can set his own values for the script parameters here
		sources = [
			'.models/simple-models/'
			]
	






