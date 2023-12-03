import wordcloud as w
import numpy as np
import matplotlib.pyplot as plt

terms = []
freqs = []
with open("outlined.csv") as file:
    for line in file:
       terms.append(line.split(",")[0])
       freqs.append(int(line.split(",")[1]))

d = dict(zip(terms, freqs))
wordcloud = w.WordCloud(collocations=False).generate_from_frequencies(d)

fig = plt.figure(frameon=False)
fig.set_size_inches(10.24,7.68)

ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)

ax.imshow(wordcloud, interpolation = 'bilinear', aspect='auto')
fig.savefig("_static/wordcloud.png")
#plt.show()