import config
import os
import sys
import subprocess
import time

RED = "\033[31m"
RESET = "\033[0m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"





class Result:
	def __init__(self, command, output, error, return_code, time, timeout = False):
		self.command = command
		self.output = output
		self.error = error
		self.return_code = return_code
		self.time = time
		self.timeout = timeout

class Controller:
	def __init__(self, target, sources = ["./models"]):
		self.target = target
		self.stop_on_first_fail = True
		self.sources = sources
		self.verbose = False
		self.timeout = 30000
		self.num_threads = 12


	def get_paths(self):

		data = {}

		for source in self.sources:
		
			print('Searching source:', source)
			if not os.path.exists(source):
				print("No files to test")
				return data

			data[source] = sorted(
				os.path.join(r, file)
				for r, d, f in os.walk(source)
				for file in f if file.endswith(self.target)
			)
		
		return data


	def run_command(self, cmd):
		
		if self.verbose:
				# put this after executing command to get input
				# and output matched better when running in threads
				print("Running:", cmd)

		start = time.perf_counter()

		with subprocess.Popen(
			cmd,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			universal_newlines=True,
			shell=True
		) as p:

			try:
				(output, err) = p.communicate(timeout=self.timeout)
				end = time.perf_counter()
				elapsed = end - start
				return Result(cmd, output, err, p.returncode, elapsed)

			except subprocess.TimeoutExpired:
				p.kill()
				(output, err) = p.communicate()
				end = time.perf_counter()
				elapsed = end - start
				return Result(cmd, "", "", p.returncode , elapsed, timeout=True)

			except Exception as e:
				print(f"Error running test: {cmd} as {e}")



