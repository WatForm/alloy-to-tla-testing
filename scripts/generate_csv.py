
from accumulator import *
import csv

def validate(accumulator):

	for k in accumulator.table:
		if not isinstance(accumulator.table[k], TestTimeResult):
			return False
		
	return True


def test1():
	ttr = TestTimeResult(1,2,3)
	acc = Accumulator()
	acc.log("null test",ttr)
	print(acc)
	print(validate(acc))

test1()