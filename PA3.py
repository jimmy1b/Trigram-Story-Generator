import random

NOT_SHERLOCK = ["alice-27.txt","london-call-27.txt", "melville-billy-27.txt", "twain-adventures-27.txt"]

ONLY_SHERLOCK = ["doyle-27.txt", "doyle-case-27.txt"]

TEST_FILE = ["test.txt"] #used for debugging

SHERLOCK_OUTPUT = "sherlock-story.txt"

ALL_OUTPUT = "six-book-story.txt"

class Node:
	def __init__(self, word, c = 1):
		self.word = word
		self.c = c
		self.nextWords = {} #dictionary of next nodes

# Creates a dictionary of trigrams that will be used to write a story
# parameters are a dictionary to make a trigram with and a type (1 or 2) to determine what files to read
def createTrigram(trigrams, type):
	bigram = None  #node
	trigram = None #node
	if type == 0:
		for fileName in TEST_FILE:
			with open(fileName, "r") as story:
				words = story.read().lower().split()
				for word in words:
					if bigram == None:
						node = Node(word)
						trigrams[word] = node
						bigram = node


					elif trigram == None:
						node2 = Node(word)
						bigram.nextWords[word] = node2
						trigram = node2
						if word in trigrams:
							trigrams[word].c += 1
							bigram = trigrams[word]
						else:
							node1 = Node(word)
							trigrams[word] = node1
							bigram = node1


					else:
						if word in trigram.nextWords:
							trigram.nextWords[word].c += 1
						else:
							trigram.nextWords[word] = Node(word)

						if word in bigram.nextWords:
							bigram.nextWords[word].c += 1
							trigram = bigram.nextWords[word]
							# if word != trigram.word:
							# 	trigram = bigram.nextWords[word]
						else:
							node2 = Node(word)
							bigram.nextWords[word] = node2
							trigram = node2

						if word in trigrams:
							trigrams[word].c += 1
							bigram = trigrams[word]
						else:
							node1 = Node(word)
							trigrams[word] = node1
							bigram = node1
	elif type == 1:
		for fileName in ONLY_SHERLOCK:
			with open(fileName, "r") as story:
				words = story.read().lower().split()
				for word in words:
					if bigram == None:
						node = Node(word)
						trigrams[word] = node
						bigram = node


					elif trigram == None:
						node2 = Node(word)
						bigram.nextWords[word] = node2
						trigram = node2
						if word in trigrams:
							trigrams[word].c += 1
							bigram = trigrams[word]
						else:
							node1 = Node(word)
							trigrams[word] = node1
							bigram = node1


					else:
						if word in trigram.nextWords:
							trigram.nextWords[word].c += 1
						else:
							trigram.nextWords[word] = Node(word)

						if word in bigram.nextWords:
							bigram.nextWords[word].c += 1
							trigram = bigram.nextWords[word]
							# if word != trigram.word:
							# 	trigram = bigram.nextWords[word]
						else:
							node2 = Node(word)
							bigram.nextWords[word] = node2
							trigram = node2

						if word in trigrams:
							trigrams[word].c += 1
							bigram = trigrams[word]
						else:
							node1 = Node(word)
							trigrams[word] = node1
							bigram = node1

	elif type == 2:
		for fileName in NOT_SHERLOCK:
			with open(fileName, "r") as story:
				words = story.read().lower().split()
				for word in words:
					if bigram == None:
						node = Node(word)
						trigrams[word] = node
						bigram = node


					elif trigram == None:
						node2 = Node(word)
						bigram.nextWords[word] = node2
						trigram = node2
						if word in trigrams:
							trigrams[word].c += 1
							bigram = trigrams[word]
						else:
							node1 = Node(word)
							trigrams[word] = node1
							bigram = node1


					else:
						if word in trigram.nextWords:
							trigram.nextWords[word].c += 1
						else:
							trigram.nextWords[word] = Node(word)


						if word in bigram.nextWords:
							bigram.nextWords[word].c += 1
							trigram = bigram.nextWords[word]
							# if word != trigram.word:
							# 	trigram = bigram.nextWords[word]
						else:
							node2 = Node(word)
							bigram.nextWords[word] = node2
							trigram = node2

						if word in trigrams:
							trigrams[word].c += 1
							bigram = trigrams[word]
						else:
							node1 = Node(word)
							trigrams[word] = node1
							bigram = node1
	return

# def findOther(wordNode, word):
# 	current = wordNode
# 	if current.word == word:
# 		return current
# 	while current.other != None:
# 		current = current.other
# 		if current.word == word:
# 			return current
# 	return current

# This method uses a trigram to create a story and write it to a file
# parameters are a dictionary of trigrams and a name for the story 
def createStory(trigrams, name):
	story = ""
	first = None
	second = None
	for i in range(1000):
		if first == None:
			# get a random key frm dictionary
			wordlist = trigrams.keys()
			rNum = random.randint(1, len(wordlist)) - 1
			first = trigrams[wordlist.pop(rNum)]
			story += str(first.word + " ")
			# print story

		elif second == None:
			rNum = random.randint(1, first.c)
			j = 0
			for w in first.nextWords:
				j = j + first.nextWords[w].c
				if j >= rNum:
					# print rNum, j
					break
			second = first.nextWords[w]
			story += str(second.word + " ")
			# print story

		else:
			rNum = random.randint(1, second.c)
			j = 0
			for w in second.nextWords:
				j += second.nextWords[w].c
				if j >= rNum:
					# print rNum, j
					break
			third = second.nextWords[w]
			story += str(third.word + " ")
			# print story
			first = trigrams[second.word]
			second = first.nextWords[third.word]
			# print 3

	# print story

	# write story to file
	with open(name, "w") as f:
		f.write(story)


#------------------------------------------------------------------------------------------------------------
# Running code


trigrams = {}
createTrigram(trigrams, 1)
createStory(trigrams, SHERLOCK_OUTPUT)
createTrigram(trigrams, 2)
createStory(trigrams, ALL_OUTPUT)
print "Done!"

#used for debugging
#
# for key in trigrams:
# 	# print key
# 	words = trigrams[key].nextWords
# 	for w in words:
# 		# print w
# 		more = words[w].nextWords
# 		for m in more:
# 			# print m
# 			print str(key + "->" + w + "->" + m)