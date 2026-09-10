class Accumulator:
	def __init__(self):
		self.table = {}
	def log(self, key, val):
		self.table[key] = val


class TestTimeResult:
	def __init__(self, translate_time, run_time, parse_time):
		self.translate_time = translate_time
		self.run_time = run_time
		self.parse_time = parse_time