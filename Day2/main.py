import pandas as pd
from sqlalchemy import create_engine

# Replace the following with your database connection details
username = 'root'  # Your MySQL username
password = 'root'  # Your MySQL password
host = 'localhost'  # Your MySQL host, e.g., 'localhost' or an IP address
database = 'test'  # Your MySQL database name

# Create a connection string using SQLAlchemy
connection_string = f'mysql+pymysql://{username}:{password}@{host}/{database}'

# Create an engine
engine = create_engine(connection_string)

# Read data from MySQL into a pandas DataFrame
df_sql = pd.read_sql('SELECT * FROM employees;', engine)

df_csv = pd.read_csv("sample.csv")

merged_dataframe = pd.merge(df_sql,df_csv,on="id",how="outer")

print(merged_dataframe.info())

