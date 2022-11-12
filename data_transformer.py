#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import os
import boto3
import random
import datetime
from time import sleep
import yfinance as yf

kinesis = boto3.client('kinesis', "us-east-2")

def lambda_handler(event, context):
   
    stocks = ["FB", "SHOP", "BYND", "NFLX", "PINS", "SQ", "TTD", "OKTA", "SNAP", "DDOG"]
    
    for stock in stocks:
        hist = yf.Ticker(stock).history(start="2022-05-02", end="2022-05-03", interval="5m")
        
        for index, row in hist.iterrows(): 
            json_string = {"high":round(row["High"], 2), "low":round(row["Low"], 2), "ts":str(index), "name":stock}
            
            data = json.dumps(json_string)+"\n"
            kinesis.put_record(StreamName="project3_datastream", Data=data, PartitionKey="partitionkey")
        
    return {
        'statusCode': 200,
        'body': json.dumps("Success")
    }

