from flask import Flask
import pandas as pd


app=Flask(__name__)

#df= pd.read_csv(r"C:\Users\sidda\Desktop\association rules\Association Rules Problem Statement\population.csv","utf-8")

@app.route('/city/name')
def sid(name):
 return " "+  name
#def get_population(name):
  ###  return "df['Population']=%d",'City'




if __name__ =="__main__":
  app.run(debug=True)