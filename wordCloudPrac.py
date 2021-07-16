from wordcloud import WordCloud
import matplotlib.pyplot as plt

text ="This data visualization technique gives us a glance at what text should be analyzed, so it is a very beneficial technique in NLP tasks"
wordcloud =WordCloud().generate(text)

plt.figure(figsize =(12,12))
plt.imshow(wordcloud)

plt.axis("off")
plt.show()