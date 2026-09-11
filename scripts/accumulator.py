class Accumulator:
	def __init__(self):
		self.table = {}
	def log(self, key, val):
		self.table[key] = val

NAME = "name"
TRANSLATION = "translation"
RUN = "run"
PARSE = "parse"

class TestTimeResult:
	def __init__(self, translate_time, run_time, parse_time):
		self.translate_time = translate_time
		self.run_time = run_time
		self.parse_time = parse_time

	def csv_fieldnames():
		return [TRANSLATION, RUN, PARSE]
	
	def csv_record(self):
		return {

			
			TRANSLATION : self.translate_time,
			RUN : self.run_time,
			PARSE: self.parse_time

		}