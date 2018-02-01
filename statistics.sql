--наиболее и наименее счастливые локации
with CTE_average as (select location,avg(tweet_sentiment) as avg_t 
                        from tweets
                        group by location)

select * from CTE_average as r
where avg_t = (select min(avg_t) from CTE_average)  or avg_t = (select max(avg_t) from CTE_average)

--наиболее и наименее счастливые пользователи
with CTE_average as (select u.name, avg(t.tweet_sentiment) avg_t 
                    from tweets t
                    inner join users u on t.user_id = u.user_id
                    where name != ''
                    group by u.name)

select * from CTE_average as r
where avg_t = (select min(avg_t) from CTE_average)  or avg_t = (select max(avg_t) from CTE_average)

--наиболее и наименее счастливые страны
with CTE_average as (select ct.country,avg(t.tweet_sentiment) avg_t 
                      from tweets t
                      inner join country_code ct on ct.country_code = t.country_code
                      group by ct.country)

select * from CTE_average as r
where avg_t = (select min(avg_t) from CTE_average)  or avg_t = (select max(avg_t) from CTE_average)