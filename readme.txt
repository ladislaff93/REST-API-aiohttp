REST API return information about cryptocurrency, save that information to database and delete information from database.
Connect to the kucoin exchange using ccxt module. API is asynchronous and build on aiohttp module. Database used is Postgresql.

What information API return? :
    1.) Name of cryptocurrency. e.g. BTC, ETH, IOI, etc.
    2.) Last price of cryptocurrency compare to USDT. e.g. BTC/USDT
    3.) Timestamp rounded to seconds. 

To get information about cryptocurrency and to save cryptocurrency into database write '/price/cryptocurrency':
    e.g. http://localhost:8080/price/BTC
To return information from database that is paginated to 10 rows write '/price/history/?page=page':
    e.g. http://localhost:8080/price/history/?page=1
To delete information from database '/price/history':
    e.g. http://localhost:8080/price/history
 
Crypto information is returned in JSON format. Database have one table name currencies and id, currency, price, date columns. 