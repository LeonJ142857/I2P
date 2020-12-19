def classic_buttons_positioning(b1, b2, b3, b4, b5, b6, b7, b8, b9, b0, pi, e, unary, binary, CE, backspace,
								add, subtract, multiply, divide, modulo, equal, abs, a_pow_2,  a_pow_b,
								comma, exp, fact, log, ln, one_over_a, plus_min, sq_root, ten_pow_a):
	# input number
	b1.grid(row=6, column=1, sticky="NSEW")
	b2.grid(row=6, column=2, sticky="NSEW")
	b3.grid(row=6, column=3, sticky="NSEW")
	b4.grid(row=5, column=1, sticky="NSEW")
	b5.grid(row=5, column=2, sticky="NSEW")
	b6.grid(row=5, column=3, sticky="NSEW")
	b7.grid(row=4, column=1, sticky="NSEW")
	b8.grid(row=4, column=2, sticky="NSEW")
	b9.grid(row=4, column=3, sticky="NSEW")
	b0.grid(row=7, column=2, sticky="NSEW")
	pi.grid(row=7, column=1, sticky="NSEW")
	e.grid(row=7, column=3, sticky="NSEW")

	# other functionalities
	unary.grid(row=1, column=1, sticky="NSEW")
	binary.grid(row=1, column=0, sticky="NSEW")
	CE.grid(row=1, column=3, sticky="NSEW")
	backspace.grid(row=1, column=4, sticky="NSEW")

	# basic operations
	add.grid(row=6, column=4, sticky="NSEW")
	subtract.grid(row=5, column=4, sticky="NSEW")
	multiply.grid(row=4, column=4, sticky="NSEW")
	divide.grid(row=3, column=4, sticky="NSEW")
	modulo.grid(row=2, column=4, sticky="NSEW")
	equal.grid(row=7, column=4, sticky="NSEW")

	# advanced operations
	abs.grid(row=2, column=2, sticky="NSEW")
	a_pow_2.grid(row=2, column=0, sticky="NSEW")
	a_pow_b.grid(row=4, column=0, sticky="NSEW")
	comma.grid(row=3, column=2, sticky="NSEW")
	exp.grid(row=2, column=3, sticky="NSEW")
	fact.grid(row=3, column=3, sticky="NSEW")
	log.grid(row=6, column=0, sticky="NSEW")
	ln.grid(row=7, column=0, sticky="NSEW")
	one_over_a.grid(row=2, column=1, sticky="NSEW")
	plus_min.grid(row=3, column=1, sticky="NSEW")
	sq_root.grid(row=3, column=0, sticky="NSEW")
	ten_pow_a.grid(row=5, column=0, sticky="NSEW")
