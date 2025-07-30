#7Filter out words shorter than 4 characters
str7=['car','bike','lorry','cruise','train']
short=list(filter(lambda  w: len(w) < 4,str7))
print(short)

