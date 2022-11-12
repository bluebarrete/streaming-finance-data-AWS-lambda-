STREAMING FINANCE DATA WITH AWS LAMBDA

This project is aiming to provision a Lambda function to be able to get near real time finance data records for downstream processing and interactive querying.
The data is collected from Yahoo finance with yfinance package and loaded into AWS S3 bucket via kinesis, AWS Glue sets up a tabular format for this data and AWS Athena are leveraged to perform interactive querying using sql.

 
<img width="497" alt="image" src="https://user-images.githubusercontent.com/42550664/201448139-7dd7cbf2-fe02-4a3c-ad74-8a3287f5695b.png">



AIM
Collecting one full day’s worth of stock price data and both HIGH and LOW prices for the 10 companies listed below on for May 2nd,2022, to May 3rd 2022, at a five minute interval.
Facebook (FB), Shopify (SHOP), Beyond Meat (BYND), Netflix (NFLX), Pinterest (PINS)
Square (SQ), The Trade Desk (TTD), Okta (OKTA), Snap (SNAP), Datadog (DDOG)







 

 





