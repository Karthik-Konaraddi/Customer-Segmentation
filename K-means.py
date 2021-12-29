import cx_Oracle
import csv
import os
import pandas as pd

path = 'C:/Users/Lakshana/project/parameters.txt'
extension='.csv'
file = open(path,'r') 
username=file.readline()
password=file.readline()
hostName=file.readline()
servicename=file.readline()
filename=file.readline()
query=file.readline()
login=username.strip('\n')+password.strip('\n')+hostName.strip('\n')+servicename.strip('\n')
#timestr = time.strftime("%Y-%m-%d--%H-%M-%S")
con = cx_Oracle.connect(login)
print("working")
filename=filename.strip('\n')
filename=filename+extension
FILE=open(filename,"w");
output=csv.writer(FILE, dialect='excel')
cur = con.cursor()
cur.execute(query.strip('\n'))
headers = [i[0] for i in cur.description]
output.writerow(headers)
for row in cur:
	output.writerow(row)
cur.close()
con.close()
FILE.close()

customer = pd.read_csv(filename)
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=5, random_state=1).fit(customer.iloc[:, 1:])
labels = kmeans_model.labels_
customer['lables'] = labels
customer.to_csv("after_clustering.csv", sep=',', encoding='utf-8',index=False)

reader = csv.reader(open("after_clustering.csv","r"))
lines=[]
next(reader)
for line in reader:
    lines.append(line)
con = cx_Oracle.connect('system/Anishapeksha01@127.0.0.1/XE')
ver=con.version.split(".")
cur=con.cursor()
cur.executemany("insert into label_clustering values (:1,:2,:3,:4,:5,:6)", lines)
con.commit ()
cur.close()
