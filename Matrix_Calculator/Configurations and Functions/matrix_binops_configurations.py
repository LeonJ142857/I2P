from tkinter import *


def configure_binops(objects_matrix_binary, matrix_binary_1, matrix_binary_2):
	# renaming for easier access
	button_create_matrix_1 = objects_matrix_binary['button_create_matrix_1'	]
	button_create_matrix_2 = objects_matrix_binary['button_create_matrix_2'	]
	frame_buttons_binary   = objects_matrix_binary['frame_buttons_binary'	]
	frame_1_up 			   = objects_matrix_binary['frame_1_up'				]
	frame_2_up 			   = objects_matrix_binary['frame_2_up'				]
	frame_1_lower 		   = objects_matrix_binary['frame_1_lower'			]
	frame_2_lower 		   = objects_matrix_binary['frame_2_lower'			]
	matrix_binary_window   = objects_matrix_binary['matrix_binary_window'	]
	m = matrix_binary_1.row_count
	n = matrix_binary_1.column_count
	output_space  = objects_matrix_binary['output_space' ]
	size_entry_1  = objects_matrix_binary['size_entry_1' ]
	size_entry_2  = objects_matrix_binary['size_entry_2' ]
	text_matrix_1 = objects_matrix_binary['text_matrix_1']
	text_matrix_2 = objects_matrix_binary['text_matrix_2']
	
	# operations buttons
	cross 					= objects_matrix_binary['cross'					]				
	dot 					= objects_matrix_binary['dot'					]					
	inner 					= objects_matrix_binary['inner'					]				
	matrix_add 				= objects_matrix_binary['matrix_add'			]
	matrix_multiplication 	= objects_matrix_binary['matrix_multiplication'	]
	outer 					= objects_matrix_binary['outer'					]
	scalar_multiplication 	= objects_matrix_binary['scalar_multiplication'	]
	solve 					= objects_matrix_binary['solve'					]
	subtract 				= objects_matrix_binary['subtract'				]

	buttons = [button_create_matrix_1, button_create_matrix_2, cross, 
		dot, inner, matrix_add, matrix_multiplication, outer,
		scalar_multiplication, solve, subtract, output_space,
		size_entry_1, size_entry_2, text_matrix_1, text_matrix_2
	]

	for widget in buttons:
		widget.grid_propagate(False)

	matrix_binary_window.title("Classic Calculator > Matrix Binary Calculator")
	matrix_binary_window.protocol("WM_DELETE_WINDOW", matrix_binary_window.withdraw)
	binary_window_width = 270 + 60 * 3 + 60 * 3 ############
	binary_window_height = 85 + max(100, 53 * 3) #########
	binary_init_x = 50 + 390
	binary_init_y = 50
	matrix_binary_window.geometry(
		f'{binary_window_width}x{binary_window_height}+{binary_init_x}+{binary_init_y}'
	)
	matrix_binary_window.resizable(width=False, height=False)

	# unary operations objects positioning
	frame_buttons_binary.grid	(row=0, column=0, rowspan=4, columnspan=3		  , sticky="NSEW")
	frame_1_up.grid				(row=0, column=3, 			 columnspan=3		  , sticky="NSEW")
	frame_2_up.grid				(row=0, column=6, 			 columnspan=3		  , sticky="NSEW")
	frame_1_lower.grid			(row=1, column=3, rowspan=3, columnspan=3		  , sticky="NSEW")
	frame_2_lower.grid			(row=1, column=6, rowspan=3, columnspan=3		  , sticky="NSEW")

	cross.grid					(row=1, column=0						 		  , sticky="NSEW")
	dot.grid					(row=1, column=1						 		  , sticky="NSEW")
	inner.grid					(row=1, column=2						 		  , sticky="NSEW")
	matrix_add.grid				(row=2, column=0						 		  , sticky="NSEW")
	matrix_multiplication.grid	(row=2, column=1						 		  , sticky="NSEW")
	outer.grid					(row=2, column=2						 		  , sticky="NSEW")
	scalar_multiplication.grid	(row=3, column=0						 		  , sticky="NSEW")
	solve.grid					(row=3, column=1						 		  , sticky="NSEW")
	subtract.grid				(row=3, column=2						 		  , sticky="NSEW")

	button_create_matrix_1.grid	(row=1, column=1						 		  , sticky="NSEW")
	button_create_matrix_2.grid	(row=1, column=1						 		  , sticky="NSEW")
	size_entry_1.grid			(row=0, column=1						 		  , sticky="NSEW")
	size_entry_2.grid			(row=0, column=1						 		  , sticky="NSEW")
	text_matrix_1.grid			(row=0, column=0						 		  , sticky="NSEW")
	text_matrix_2.grid			(row=0, column=0						 		  , sticky="NSEW")
	output_space.grid			(row=0, column=0		   , columnspan=3, ipady=2, sticky="NSEW")

	size_entry_1.insert(INSERT, "3 x 3")
	size_entry_2.insert(INSERT, "3 x 3")
	output_space.insert(INSERT, "This is where you will see the output.")
