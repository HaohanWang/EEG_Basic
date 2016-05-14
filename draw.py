from matplotlib import pyplot

data = [line.strip() for line in open('reTag/rawScore')]
x = []
for line in data:
    x.append(int(line))
pyplot.hist(x, 7)
pyplot.show()