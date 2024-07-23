sentence : str = "the quick brown fox jumps over the lazy dog"
fox_index = sentence.find("fox")
if fox_index == -1:
    fox_index = -1
countof_the = sentence.count("the")
print("index of 'fox' is",fox_index)
print("'the' appears",countof_the,"times")
