from random import randint

"""
Author: Marcos Lopez - 2010
scidentifyweb@gmail.com

Practice notation skills on Bass and Treble

The goal for this is to remember a quick bass/treble space/line number 
to note identification to improve sight reading speed



TODO:
Bass/Treble combinations
Visual Identification

"""

bass_line = {
	'one':'g',
	'two':'b',
	'three':'d',
	'four':'f',
	'five':'a',
}
bass_space = {
	'one':'a',
	'two':'c',
	'three':'e',
	'four':'g',
}
treble_line = {
	'one':'e',
	'two':'g',
	'three':'b',
	'four':'d',
	'five':'f',
}
treble_space = {
	'one':'f',
	'two':'a',
	'three':'c',
	'four':'e',
}

types = ['bass','treble']
space_line = ['line','space']
line = ['one','two','three','four','five']
space = ['one','two','three','four']


level = """
Select the difficulty level

	1 - Hardest (1 second to Respond)
	2 - Hard (2 Second Response)
	3 - OK (3 Second Response)

"""
lvl = raw_input(level)

random_type = randint(0, len(types)-1)
random_space_line = randint(0, len(space_line)-1)
random_space = randint(0, len(space)-1)
random_line = randint(0, len(line)-1)

count = int(raw_input('How many questions? '))


c = 0
while c < count:
	random_type = randint(0, len(types)-1)
	random_space_line = randint(0, len(space_line)-1)
	random_space = randint(0, len(space)-1)
	random_line = randint(0, len(line)-1)

	
	question = '%s %s # ' % (
		types[random_type], space_line[random_space_line]
	)
	if space_line[random_space_line] == 'line':
		question += '%s ' % (line[random_line])
		answer_str = '%s_%s' % (types[random_type], space_line[random_space_line])
		k = str(line[random_line])
		answer = eval('%s' % (answer_str))[k]

	if space_line[random_space_line] == 'space':
		question += '%s ' % (line[random_space])
		answer_str = '%s_%s' % (types[random_type], space_line[random_space_line])
		k = str(space[random_space])
		answer = eval('%s' % (answer_str))[k]

	

	question += ': '

	r= str(raw_input(question))
	#time.sleep(lvl)
	
	if r == answer:
		print 'youre cool!'
		print ''
	else:
		print 'YOU FUCKING SUCK'
		print ''
		print 'Answer was: %s' % answer
		print ''
		
	c+=1
	
		




