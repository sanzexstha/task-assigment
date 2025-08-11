# import pickle

# # Replace with your file path
# file_path = "E-3.pkl"

# # Open in binary read mode and load
# with open(file_path, "rb") as f:
#     data = pickle.load(f)

# # Now 'data' contains whatever object was saved in the .pkl file
# print(type(data))
# print(data)


import pickle
import numpy as np


test = np.load('E-4.npy')

bool_arr = test.astype(bool)


# Save as pickle
with open("E-4.pkl", "wb") as f:
    pickle.dump(bool_arr, f)
print(bool_arr.shape)
print(bool_arr)


# Replace with your file path
# file_path = "E-4_labels.npy"

# with open(file_path, 'rb') as file:
#         data = pickle.load(file)
# print(type(data))   # Usually <class 'numpy.ndarray'>
# print(data.shape)   # Shape of the array
# print(data)         # Contents

# import pandas as pd
# df = pd.read_pickle("E-6.pkl")
# print(df.head())


# import pandas as pd
# file = 'labeled_anomalies.csv'
# values = pd.read_csv(file)
# values = values[values['spacecraft'] == 'SMAP']
# filenames = values['chan_id'].values.tolist()
# for fn in filenames:
#     # train = np.load(f'{dataset_folder}/train/{fn}.npy')
#     test = np.load('E-4.npy')
#     # train, min_a, max_a = normalize3(train)
#     # test, _, _ = normalize3(test, min_a, max_a)
#     # np.save(f'{folder}/{fn}_train.npy', train)
#     # np.save(f'{folder}/{fn}_test.npy', test)
#     labels = np.zeros(test.shape[0])
#     indices = values[values['chan_id'] == fn]['anomaly_sequences'].values[0]
#     indices = indices.replace(']', '').replace('[', '').split(', ')
#     indices = [int(i) for i in indices]
#     for i in range(0, len(indices), 2):
#         labels[indices[i]:indices[i+1]] = 1
#     np.save(f'{fn}_labels.npy', labels)