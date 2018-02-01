create table if not exists users (user_id integer primary key not null, name text);
create table if not exists country_code (country_code text  primary key not null, country text);

insert into users
select distinct user_id, name from tweets;

insert into country_code
select distinct country_code, country name from tweets
where country_code is not null;

ALTER TABLE tweets RENAME TO tweets_old;

create table tweets
(tweet_id integer primary key not null
,user_id integer  
, tweet_text text
, country_code text 
, display_url text
, lang text
, created_at text
, location text
, tweet_sentiment integer
,CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users (user_id)
,CONSTRAINT fk_country_code FOREIGN KEY (country_code) REFERENCES country_code (country_code));

insert into tweets 
select tweet_id, user_id,tweet_text,country_code,display_url,lang,created_at,location,tweet_sentiment from tweets_old;

drop table tweets_old;
