import pymongo
import pandas as pd
import json

#provide the mongodb url to connect python to mongobd
client = pymongo.MongoClient('mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority')

#provide mongodb localhost to connect python to mongo db
#client = pymongo.MongoClient('mongodb://localhost:27017')

DATABASE_NAME = 'aps3'
COLLECTION_NAME ='sensor'
DATA_FILE_PATH = r"E:\DATA_SCIENCE\ML_projects\aps_sensor_fault\aps_failure_training_set1.csv"

if __name__ =="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns: {df.shape}")

    #convert dataframe into json so that we can dump this data in Mongodb
    df.reset_index(drop=True, inplace=True)
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert json data into mongobd 
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    print("inserted")
