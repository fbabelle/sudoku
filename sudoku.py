import pandas as pd
import numpy as np
import math
import copy

# given a matrix and the value of an element, find the position of this value within the matrix
def returnindex(x, mtx):
	if x != 0:
		rowidx = 0
		for i in xrange(len(mtx)):
			try:
				columnidx = mtx[i].tolist().index(x)   # otherwise return attributeerror: ndarray has no attribute .index()
				break
			except ValueError:
				if i == len(mtx)-1:
					print "this value not in matrix..."
					return [-1, -1]
				rowidx += 1
				next
	else:
		print "can't find the index of '0's..."
		return [-1, -1]
	return [rowidx, columnidx]

def addpossiblenbr(i, j, a, b):
	value_matrix = copy.copy(a)
	working_matrix = copy.copy(b)
	certain_row = []
	certain_col = []
	certain_sec = []
	if value_matrix[i][j] == 0:
		for m in value_matrix[i]:
			if m != 0:
				certain_row.append(m)
		for n in value_matrix[:,j]:
			if n != 0:
				certain_col.append(n)

		section_index = [i/3*3, j/3*3]
		for p in xrange(section_index[0], section_index[0]+3):
			for q in xrange(section_index[1], section_index[1]+3):
				if value_matrix[p][q] != 0:
					certain_sec.append(value_matrix[p][q])

		certain_row_col = certain_row
		for x in certain_col:
			if x not in certain_row_col:
				certain_row_col.append(x)
		for x in certain_sec:
			if x not in certain_row_col:
				certain_row_col.append(x)

		for y in [1,2,3,4,5,6,7,8,9]:
			if y not in certain_row_col and y not in working_matrix[i][j]:
				working_matrix[i][j].append(y)
	else:
		return (value_matrix, working_matrix)

	return (value_matrix, working_matrix)

# update 2 matrix
def update_valuemtx(a, b):
	value_matrix = copy.copy(a)
	working_matrix = copy.copy(b)
	for i in xrange(9):
		for j in xrange(9):
			if len(working_matrix[i][j]) == 1:   # give value to cells with only one solution (working matrix only has 1 value included)
				if value_matrix[i][j] == 0:  # pay attention ################################################
					value_matrix[i][j] = working_matrix[i][j][0]
				# delete row duplicate
				for m in working_matrix[i]:
					if (value_matrix[i][j] in m) and (len(m) > 1):
						m.remove(value_matrix[i][j])
				# delete column duplicate
				for n in xrange(9):
					if (value_matrix[i][j] in working_matrix[n][j]) and (len(working_matrix[n][j]) > 1):
						working_matrix[n][j].remove(value_matrix[i][j])
				# delete section duplicate
				section_index = [i/3*3, j/3*3]
				for p in xrange(section_index[0], section_index[0]+3):
					for q in xrange(section_index[1], section_index[1]+3):
						if (value_matrix[i][j] in working_matrix[p][q]) and (len(working_matrix[p][q]) > 1):
							working_matrix[p][q].remove(value_matrix[i][j])

	# check if a number only appears in section once, if so, the spot should be filled with that number
	# 13 8 9
	# 43 7 5
	# 43 6 2     then 13 can only be 1 because 1 appears nowhere else.
	for i in xrange(9):
		for j in xrange(9):
			section_index = [i/3*3, j/3*3]
			section_ele = []
			for p in xrange(section_index[0], section_index[0]+3):
				for q in xrange(section_index[1], section_index[1]+3):
					if value_matrix[p][q] == 0:
						for itr in working_matrix[p][q]:
							section_ele.append(itr)
			# print section_ele
			for p in xrange(section_index[0], section_index[0]+3):
				for q in xrange(section_index[1], section_index[1]+3):
					if len(working_matrix[p][q]) > 1:
						for itr in working_matrix[p][q]:
							if section_ele.count(itr) == 1:
								# print p, q, itr
								value_matrix[p][q] = itr
								working_matrix[p][q] = [itr]
								break

	return (value_matrix, working_matrix)

def validation(a):
	value_matrix = copy.copy(a)
	# working_matrix = b
	cell_validation = []
	sum_validation = []
	# all cells have values
	for i in xrange(9):
		for j in xrange(9):
			if bool(value_matrix[i][j]):
				cell_validation.append(1)
			else:
				cell_validation.append(0)
	# row sum equals 45
	for i in xrange(9):
		if sum(value_matrix[i]) == 45:
			sum_validation.append(1)
		else:
			sum_validation.append(0)
	# column sum equals 45
	for j in xrange(9):
		add = 0
		for row_itr in xrange(9):
			add += value_matrix[row_itr, j]
		if add == 45:
			sum_validation.append(1)
		else:
			sum_validation.append(0)
	# section sum equals 45
	for m in [0, 3, 6]:
		for n in [0, 3, 6]:
			add = 0
			for x in xrange(m, m+3):
				for y in xrange(n, n+3):
					add += value_matrix[x][y]
			if add == 45:
				sum_validation.append(1)
			else:
				sum_validation.append(0)

	if np.mean(cell_validation) == 1 and np.mean(sum_validation) == 1:
		return 1
	else:
		return 0


def tryanderror(a, b):
	# print a
	# print b
	value_matrix = fuckingnoob(a)
	working_matrix = fuckingnoob(b)

	# value_matrix_tne = copy.deepcopy(value_matrix)
	# working_matrix_tne = copy.deepcopy(working_matrix)
	value_matrix_tne = fuckingnoob(value_matrix)
	working_matrix_tne = fuckingnoob(working_matrix)
	# working_matrix_tne[0][1].remove(8)
	# print working_matrix_tne
	# print working_matrix

	for length in xrange(2, 5):
		# print value_matrix_tne
		# print working_matrix_tne
		for i in xrange(9):
			for j in xrange(9):
				# print i,j, length
				if len(working_matrix_tne[i][j]) == length:
					for itr in xrange(length):
						print "length: %d itr: %d" % (length, itr)
						try:
							working_matrix_tne[i][j].remove(working_matrix_tne[i][j][itr])
							# print working_matrix_tne
							# value_matrix_tne[i][j] = working_matrix_tne[i][j][itr]
							for x in xrange(10):
								result = update_valuemtx(value_matrix_tne, working_matrix_tne)
								value_matrix_tne = result[0]
								working_matrix_tne = result[1]
							if validation(value_matrix_tne):
								print "success...at [%d, %d] with value %d" % (i, j, value_matrix_tne[i][j])
								return (value_matrix_tne, working_matrix_tne)
								# break
							else:
								print "fail...at [%d, %d] with value %d" % (i, j, value_matrix_tne[i][j])
								# print value_matrix_tne
								value_matrix_tne = fuckingnoob(value_matrix)
								# print value_matrix_tne
								working_matrix_tne = fuckingnoob(working_matrix)
								# print working_matrix_tne
								# next
						except IndexError:
							# print "raise exception..."
							value_matrix_tne = fuckingnoob(value_matrix)
							working_matrix_tne = fuckingnoob(working_matrix)
							print "raise exception..."
							print working_matrix_tne
							continue

	return (value_matrix_tne, working_matrix_tne)


# fucking python can't just copy a list
def fuckingnoob(x):
	noobs = copy.deepcopy(x)
	return noobs


# main codes
path = "D:\sudoku\\"
df = pd.read_csv(path+'sudoku_input.csv')

nbr_mtx = (len(df)+1)/10
print "number of matrixes: ", nbr_mtx

output_df = pd.DataFrame(columns=df.columns)
blankline_df = pd.DataFrame([['','','','','','','','','']], columns=df.columns)
for i in xrange(nbr_mtx):
	sudoku = df[i*10:i*10+9]
	sudoku = sudoku.as_matrix()

	# step 1 adding pre-existing numbers
	allmtx = [ [ [] for i in xrange(9)] for j in xrange(9)]
	for i in xrange(len(sudoku)):
		for j in xrange(len(sudoku[0])):
			if sudoku[i][j] != 0:
				allmtx[i][j].append(sudoku[i][j])

	# step 2 adding all possible numbers to working_matrix
	for i in range(9):
		for j in range(9):
			result = addpossiblenbr(i, j, sudoku, allmtx)
			sudoku = result[0]
			allmtx = result[1]

	# step 3 basic update numbers
	for itr in xrange(3):
		result = update_valuemtx(sudoku, allmtx)
		sudoku = result[0]
		allmtx = result[1]

	# step 4 strategical supposition
	result = tryanderror(sudoku, allmtx)
	sudoku = result[0]
	allmtx = result[1]

	# # validation
	print validation(sudoku) == True
	sudoku_df = pd.DataFrame(sudoku, columns=df.columns)
	# print sudoku
	
	output_df = pd.concat([output_df, sudoku_df], axis=0)
	output_df = pd.concat([output_df, blankline_df], axis=0)

output_df.to_csv(path+'sudoku_output.csv', index=False)
