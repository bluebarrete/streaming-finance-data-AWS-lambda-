STREAMING FINANCE DATA WITH AWS LAMBDA

This project is aiming to provision a Lambda function to be able to get near real time finance data records for downstream processing and interactive querying.
The data is collected from Yahoo finance with yfinance package and loaded into AWS S3 bucket via kinesis, AWS Glue sets up a tabular format for this data and AWS Athena are leveraged to perform interactive querying using sql.

 
<img width="497" alt="image" src="https://user-images.githubusercontent.com/42550664/201448139-7dd7cbf2-fe02-4a3c-ad74-8a3287f5695b.png">



AIM
Collecting one full day’s worth of stock price data and both HIGH and LOW prices for the 10 companies listed below on for May 2nd,2022, to May 3rd 2022, at a five minute interval.
Facebook (FB), Shopify (SHOP), Beyond Meat (BYND), Netflix (NFLX), Pinterest (PINS)
Square (SQ), The Trade Desk (TTD), Okta (OKTA), Snap (SNAP), Datadog (DDOG)


KINESIS DATA FIREHOSE STREAM MONITORING:

<img width="369" alt="image" src="https://user-images.githubusercontent.com/42550664/201448151-47c56116-ed41-48b5-8343-43be046a9b8f.png">

<img width="417" alt="image" src="https://user-images.githubusercontent.com/42550664/201448158-ff2cf135-53c4-430b-9b16-ebb306edfd17.png">



 

 



LAMBDA FUNCTION EXECUTION RESULTS:

<img width="438" alt="image" src="https://user-images.githubusercontent.com/42550664/201448165-b5140578-6c53-4179-8334-d38ad2bfee8d.png">



 

 





