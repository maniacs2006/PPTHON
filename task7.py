sentence : str ="   Python is fun!   "
strip_sentence = sentence.strip()
left_side = strip_sentence.ljust(18, '*')
right_side = strip_sentence.rjust(18, '*')
print(strip_sentence)
print(left_side)
print(right_side)