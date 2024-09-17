import json
import requests
import pandas as pd

def lambda_handler(event, context):
    
    print("Event Data -> ", event)
    response = requests.get("https://www.google.com/")
    print(response.text)

    d = {'col1':[1,2,3,4],'col2':[5,6,7,8]}
    df = pd.DataFrame(d)
    print(df)
    print("demo completed")