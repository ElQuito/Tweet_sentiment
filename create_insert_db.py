import sqlite3
import json

conn = sqlite3.connect("tweets.db") 
cursor = conn.cursor()

#создание таблицы
cursor.execute("""create table if not exists tweets
                  (tweet_id integer primary key not null,user_id integer, name text, tweet_text text, country_code text,country text, display_url text, lang text, created_at text, location text, tweet_sentiment integer)
               """)
			   

#открываем файл	и записываем в базу
with open('three_minutes_tweets.json.txt') as f:
	for line in f:
		content_tweets = json.loads(line)
		#проверяем на содержание объектов в словаре
		if 'created_at' in content_tweets:
			try:
				user_id = content_tweets['user']['id']
			except TypeError:
				user_id = None
			try:
				name = content_tweets['user']['name']
			except TypeError:
				name = None
			try:
				country_code = content_tweets['place']['country_code']
			except TypeError:
				country_code = None
			try:
				country = content_tweets['place']['country']
			except TypeError:
				country = None
			try:
				display_url = content_tweets['user']['url']
			except TypeError:
				display_url = None
			try:
				lang = content_tweets['lang']
			except TypeError:
				lang = None
			try:
				location = content_tweets['user']['location']
			except TypeError:
				location = None
			try:
				cursor.execute("INSERT INTO tweets (tweet_id,user_id,name,tweet_text,country_code,country,display_url,lang,created_at,location) VALUES (?,?,?,?,?,?,?,?,?,?)",(content_tweets['id'],user_id,name,content_tweets['text'],country_code,country,display_url,lang,content_tweets['created_at'],location))
			except sqlite3.IntegrityError as e:
				#выводим задублированные твиты
				print(e,content_tweets['id'])
		
		#проверяем на содержание объектов в словаре (ретвиты)
		if 	'retweeted_status' in content_tweets:
			try:
				user_id = content_tweets['retweeted_status']['user']['id']
			except TypeError:
				user_id = None
			try:
				name = content_tweets['retweeted_status']['user']['name']
			except TypeError:
				name = None
			try:
				country_code = content_tweets['retweeted_status']['place']['country_code']
			except TypeError:
				country_code = None
			try:
				country = content_tweets['retweeted_status']['place']['country']
			except TypeError:
				country = None
			try:
				display_url = content_tweets['retweeted_status']['user']['url']
			except TypeError:
				display_url = None
			try:
				lang = content_tweets['retweeted_status']['lang']
			except TypeError:
				lang = None
			try:
				location = content_tweets['retweeted_status']['user']['location']
			except TypeError:
				location = None
			try:
				cursor.execute("INSERT INTO tweets (tweet_id,user_id,name,tweet_text,country_code,country,display_url,lang,created_at,location) VALUES (?,?,?,?,?,?,?,?,?,?)",(content_tweets['retweeted_status']['id'],user_id,name,content_tweets['retweeted_status']['text'],country_code,country,display_url,lang,content_tweets['retweeted_status']['created_at'],location))
			except sqlite3.IntegrityError as e:
				#выводим задублированные твиты
				print(e,content_tweets['retweeted_status']['id'])
conn.commit()