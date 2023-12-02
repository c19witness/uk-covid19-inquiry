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

plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis("off")
plt.savefig("wordcloud.svg")
plt.show()