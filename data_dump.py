import pymongo
import pandas as pd
import json
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATABASE_NAME = "aps1"
COLLECTION_NAME="sensor1"
DATA_PATH="/config/workspace/aps_failure_training_set1.csv"


if __name__=="__main__":
    df=pd.read_csv(DATA_PATH)
    print("Rows and Columns:{df.shape}")

    df.reset_index(drop=True,inplace=True)

    json_record= list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)