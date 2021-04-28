import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mongodb:///?Server=MyServer&;Port=27017&Database=test&User=test&Password=Password")
#engine = create_engine("https://cloud.mongodb.com/v2#/org/6082fa04cfcfc8664d3e5db3")

df = pandas.read_sql("SELECT * FROM urls_aggregated LIMIT 10", engine)

df.plot(kind="bar", x="borough", y="cuisine")
plt.show()