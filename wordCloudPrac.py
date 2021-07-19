from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

x, y = np.ogrid[:300, :300]
mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)

text ="This data visualization technique gives us a glance at what text should be analyzed, so it is a very beneficial technique in NLP tasks"
wordcloud =WordCloud(background_color="white",mask=mask, contour_width=0.1, contour_color="black").generate(text)

plt.figure(figsize =(12,12))
plt.imshow(wordcloud)

plt.axis("off")
plt.show()