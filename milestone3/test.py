import pandas as pd


'''
Some test cases of data_preprocess.ipynb.

Please run data_preprocess.ipynb before test.py so that all data files are generated.

Specifically, training_order_data.csv is too larger to upload on github.

'''

# Import training cluster_map
df_read = pd.read_csv('data/cluster_map.csv', index_col=0)
cluster_map_read = df_read.to_dict('dict')['0']

print('#########################################')
print('number of districts:', len(cluster_map_read))
    
# Import training order_data
order_info_read = pd.read_csv('data/training_order_data.csv')

order_id = order_info_read['order_id']
driver_id = order_info_read['driver_id']
passenger_id = order_info_read['passenger_id']
start_district_hash = order_info_read['start_district_hash']
dest_district_hash = order_info_read['dest_district_hash']
price = order_info_read['price']
time_stamp = order_info_read['time_stamp']

order_id_num = len(order_id)
order_id_num_unique = len(order_id.unique())
print('total order_id:', order_id_num)
print('unique order_id:', order_id_num_unique)

driver_id_null = pd.isnull(driver_id)
driver_id_num = len(driver_id)
driver_id_num_unique = len(driver_id.unique())
driver_id_num_null = len(driver_id[driver_id_null])
print('total driver_id:', driver_id_num)
print('unique driver_id:', driver_id_num_unique)
print('null driver_id:', driver_id_num_null)
print('fraction of missed orders:', float(driver_id_num_null) / float(driver_id_num))
print('fraction of received orders:', 1.0 - float(driver_id_num_null) / float(driver_id_num))

    
    
