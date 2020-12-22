def create_matrix(matrix, size_entry):
	m = size_entry.get()[0]
	n = size_entry.get()[4]
	cond1 = isinstance(eval(m), (int, float))
	cond2 = isinstance(eval(n), (int, float))
	cond3 = size_entry.get()[2]
	if cond1 and cond2 and cond3:
		matrix.create_matrix(eval(m), eval(n))
