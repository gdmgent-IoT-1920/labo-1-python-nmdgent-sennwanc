
sentence = input("Welke zin wil u omdraaien ?: ");

def split_sentence(words): 
	word = words.split(" ")
	print(word)

	for i in reversed(word):
		print(i, end = ' ')

split_sentence(sentence)