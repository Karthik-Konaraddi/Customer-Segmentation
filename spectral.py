import pandas as pd
import cx_Oracle
import time
import numpy
start_time = time.time()

## db parameters
query = 'select * from clustering'

## connect to the DW and query the data
con = cx_Oracle.connect('system/Anishapeksha01@127.0.0.1/XE')
curs = con.cursor()
curs.execute(query)


## Convert the cx_Oracle object to pandas dataframe

headers = [ x[0] for x in curs.description]
data = curs.fetchall()
customer = pd.DataFrame( data, columns=headers)
from sklearn.cluster import SpectralClustering
kmeans_model = SpectralClustering(n_clusters=5, eigen_solver='arpack',affinity='nearest_neighbors',random_state=1).fit(customer.iloc[:, 1:])
labels = kmeans_model.labels_
customer['lables'] = labels
print(customer)
#customer.to_csv("after_clustering.csv", sep=',', encoding='utf-8',index=False)

dataframe_list = customer.values.tolist() # convert the dataframe to list 
sql = 'INSERT INTO label_clustering values (:1,:2,:3,:4,:5,:6)'
for index,elem in enumerate(dataframe_list): #iterating the list using index(int)
       curs.execute(sql,dataframe_list[index]) #here cursor is using the existing cursor objec
       con.commit() #committing the changes to the table
print("--- %s seconds ---" % (time.time() - start_time))
curs.close()
con.close()