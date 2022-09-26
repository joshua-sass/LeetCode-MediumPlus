import math 

def get_num_stickers(string):
	inputted = string.replace(" ", "")
	facebook = {"f":0, "a":0, "c":0, "e":0, "b":0, "o":0, "k":0}
	
	for letter in inputted:
		facebook[letter] = facebook[letter]+1

	facebook["o"] = math.ceil(facebook["o"]/2)
	max_key = max(facebook, key=facebook.get)
	return facebook[max_key]

def main():
	print(get_num_stickers("coffee kebab"))
	print(get_num_stickers("book"))
	print(get_num_stickers("ffacebook"))

if __name__ == '__main__':
	main()