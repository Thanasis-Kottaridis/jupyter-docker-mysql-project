import pymysql
from sqlalchemy import create_engine
import pandas as pd
myhost = 'mysql'

def setUpMySql(engine):
    try:
        myDB = "breastcancer"
        engine.execute("CREATE DATABASE IF NOT EXISTS {};".format(myDB)) #create db
        # engine.execute("USE {}}".format(myDB)) # select new db

        # read dataframe from datasets directory
        cancer_df = pd.read_csv("/src/datasets/breast_cancer_data.csv")
        updloadTableFromDF(cancer_df,"breastdataset",False)
        print("Done")
    except Exception as err:
        print("My SQL Manager Exception: {}".format(err.message))

def updloadTableFromDF(df,table_name, index=True):
    try:
        con_str = 'mysql+pymysql://root:root@{0}:3306/{1}'.format(myhost, "breastcancer")
        engine = create_engine(con_str)

        df.to_sql(name = table_name, con = engine, if_exists = 'replace',index=index)
        # df.to_sql(con=cnx, name=table_name, if_exists='replace', index = False)
        print("Done")
    
    except Exception as err:
        print("My SQL Manager Exception: {}".format(err.message))

def fetchBreastData():
    try:
        con_str = 'mysql+pymysql://root:root@{0}:3306/{1}'.format(myhost, "breastcancer")
        con = create_engine(con_str)

        df = pd.read_sql("SELECT * FROM breastcancer.breastdataset", con=con)
    except Exception as err:
        df = pd.read_csv("/src/datasets/breast_cancer_data.csv")
    return df

if __name__ == "__main__":
    print("Im mySQL manager")
    con_str = 'mysql+pymysql://root:root@{0}:3306'.format(myhost)
    engine = create_engine(con_str)
    # set up mySQL
    setUpMySql(engine)                       