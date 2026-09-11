
from accumulator import *
import csv

def validate(accumulator):

	for k in accumulator.table:
		if not isinstance(accumulator.table[k], TestTimeResult):
			return False
		
	return True

def write_csv(filename, testTimeResults):

	with open(filename, 'w', newline='', encoding='utf-8') as file:
		writer = csv.DictWriter(file, fieldnames=TestTimeResult.csv_fieldnames())
		writer.writeheader()
		writer.writerows([x.csv_record() for x in testTimeResults])


def test1():
	ttr = TestTimeResult(1,2,3)
	acc = Accumulator()
	acc.log("null test",ttr)
	print(acc)
	print(validate(acc))




def test2():
	ttrs = [
		TestTimeResult(1,2,3),
		TestTimeResult(1,2,4),
		TestTimeResult(1,2,5),
		TestTimeResult(1,2,6)
	]
	write_csv("test.csv", ttrs)


test1()
test2()