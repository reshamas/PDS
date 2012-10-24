#Analytics with SQL

#How many shops are there?
SELECT count(*) 
FROM shops;
#80235

#What is the average price over all listings? What is the average “price” across all transactions?
SELECT avg(price) 
FROM listings;
#2.6321
SELECT avg(price) 
FROM transactions; 
# '19.1653'


#What is the average individual price of each listing purchased (note that the price field in the transactions table is the total price for the transaction; you need to control for quantity). How does this compare to the average listing price?
SELECT avg(price/quantity) as avgp
FROM transactions;
#'19.04207566'

#Other possible interpretations
SELECT listing_id, avg(CAST(price AS DECIMAL)/CAST(quantity AS DECIMAL)) as avgp
FROM transactions
GROUP BY listing_id;

SELECT avg(p)
FROM (
	SELECT distinct listing_id, (CAST(price AS DECIMAL)/CAST(quantity AS DECIMAL)) as p
	FROM transactions
	GROUP BY listing_id) q;
#'19.08195266'

SELECT avg(p)
FROM (
	SELECT distinct listing_id, avg((CAST(price AS DECIMAL)/CAST(quantity AS DECIMAL))) as p
	FROM transactions
	GROUP BY listing_id) q;
#'19.082496194985'


#Remove listings with a price or quantity of 0 and recompute the average price. How does this compare to the average price of each listing purchased?
SELECT avg(price/quantity) as avgp
FROM transactions
WHERE quantity > 0 AND price > 0;
#19.09324607

#What are the 5 most expensive listings?
SELECT * 
FROM listings 
ORDER BY price DESC
LIMIT 5;
#Listing ids
#1075313644035
#496135414032
#220898782232
#167911416628
#321701224502

#How many listings has each user purchased? 
SELECT u.user_id, coalesce(q.cnt, 0)
FROM users u
LEFT JOIN (
	SELECT user_id, count(distinct (listing_id)) as cnt
	FROM transactions
	GROUP BY user_id
	) as q ON u.user_id = q.user_id
#ORDER BY q.cnt
LIMIT 10;

#Compute the distribution of how many users purchase different numbers of listings (# listings purchased vs. # users with that many purchases). You can ignore users with 0 purchases. 
SELECT q.cnt, count(user_id)
FROM (
	SELECT user_id, count(distinct (listing_id)) as cnt
	FROM transactions
	GROUP BY user_id)  q
GROUP BY q.cnt
ORDER BY q.cnt;
/*	1	86029
	2	4483
	3	841
	4	244
	5	122
	6	45
	7	31
	8	15
	9	3
	10	7
	11	5
	12	2
	13	2
	14	1
	15	1
	16	1
	19	1
	20	1 */

#Compute the number of users with each gender.
SELECT gender, count(gender)
FROM users 
GROUP BY gender;
#		189
#	female	508124
#	male	92932
#	private	398654

#Among the users with purchases, compute the number of users with each gender.
SELECT gender, count(distinct u.user_id)
FROM users u JOIN transactions t ON u.user_id = t.user_id
GROUP BY gender;
# OR
SELECT gender, count(distinct u.user_id)
FROM users u, transactions t 
WHERE u.user_id = t.user_id
GROUP BY gender;
#		12
#	female	2670
#	male	166
#	private	2239