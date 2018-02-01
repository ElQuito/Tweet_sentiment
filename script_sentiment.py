import sqlite3

#создаем словарь и заполняем с файла
dictionary = {}   
with open("AFINN-111.txt") as f:
  dictionary = dict(x.rstrip().split('	', 1) for x in f) 

conn = sqlite3.connect("tweets.db") 
cursor = conn.cursor()

#запрашиваем твиты где нет tweet_sentiment
cursor.execute('select tweet_id, tweet_text from tweets where tweet_sentiment is null;')

#находим совпадения из словаря
for row in cursor.fetchall():
	#по умолчанию sentiment ноль
	sentiment = 0
	# приводим к нижниму регистру и разбиваем на слова
	tweet_text = row[1].lower()
	tweet_words = tweet_text.split(' ')
	#находим слова в справочнике и ищем среднее значение
	for key in dictionary.keys():
		for word in tweet_words: 
			if  key  in word:
				sentiment = int(dictionary.get(key)) + sentiment
	if sentiment != 0:
		sentiment = sentiment/len(tweet_words)
	#обновляем значение tweet_sentiment
	cursor.execute("UPDATE tweets SET tweet_sentiment = ? WHERE tweet_id = ?;",(sentiment,row[0]))
conn.commit()