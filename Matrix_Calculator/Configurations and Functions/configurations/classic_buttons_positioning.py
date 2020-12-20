def classic_buttons_positioning(button_objects_classic):
	# input number positioning
	button_objects_classic['b1'].grid(row=6, column=1, sticky="NSEW")
	button_objects_classic['b2'].grid(row=6, column=2, sticky="NSEW")
	button_objects_classic['b3'].grid(row=6, column=3, sticky="NSEW")
	button_objects_classic['b4'].grid(row=5, column=1, sticky="NSEW")
	button_objects_classic['b5'].grid(row=5, column=2, sticky="NSEW")
	button_objects_classic['b6'].grid(row=5, column=3, sticky="NSEW")
	button_objects_classic['b7'].grid(row=4, column=1, sticky="NSEW")
	button_objects_classic['b8'].grid(row=4, column=2, sticky="NSEW")
	button_objects_classic['b9'].grid(row=4, column=3, sticky="NSEW")
	button_objects_classic['b0'].grid(row=7, column=2, sticky="NSEW")
	button_objects_classic['pi'].grid(row=7, column=1, sticky="NSEW")
	button_objects_classic['e'].grid(row=7, column=3, sticky="NSEW")

	# other functionality positioning
	button_objects_classic['unary'].grid(row=1, column=1, sticky="NSEW")
	button_objects_classic['binary'].grid(row=1, column=0, sticky="NSEW")
	button_objects_classic['CE'].grid(row=1, column=3, sticky="NSEW")
	button_objects_classic['backspace'].grid(row=1, column=4, sticky="NSEW")

	# basic operations positioning
	button_objects_classic['add'].grid(row=6, column=4, sticky="NSEW")
	button_objects_classic['subtract'].grid(row=5, column=4, sticky="NSEW")
	button_objects_classic['multiply'].grid(row=4, column=4, sticky="NSEW")
	button_objects_classic['divide'].grid(row=3, column=4, sticky="NSEW")
	button_objects_classic['modulo'].grid(row=2, column=4, sticky="NSEW")
	button_objects_classic['equal'].grid(row=7, column=4, sticky="NSEW")

	# advanced operations positioning
	button_objects_classic['abs'].grid(row=2, column=2, sticky="NSEW")
	button_objects_classic['a_pow_2'].grid(row=2, column=0, sticky="NSEW")
	button_objects_classic['a_pow_b'].grid(row=4, column=0, sticky="NSEW")
	button_objects_classic['comma'].grid(row=3, column=2, sticky="NSEW")
	button_objects_classic['exp'].grid(row=2, column=3, sticky="NSEW")
	button_objects_classic['fact'].grid(row=3, column=3, sticky="NSEW")
	button_objects_classic['log'].grid(row=6, column=0, sticky="NSEW")
	button_objects_classic['ln'].grid(row=7, column=0, sticky="NSEW")
	button_objects_classic['one_over_a'].grid(row=2, column=1, sticky="NSEW")
	button_objects_classic['plus_min'].grid(row=3, column=1, sticky="NSEW")
	button_objects_classic['sq_root'].grid(row=3, column=0, sticky="NSEW")
	button_objects_classic['ten_pow_a'].grid(row=5, column=0, sticky="NSEW")
