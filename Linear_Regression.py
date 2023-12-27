import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd


#####__Col1_fileData được coi là Y, cột 2-->n thuộc Z, mô hình với Y và Z đã biết ta cần xác định ma trận tham số \Beta
###___và ma trận \sigma^2 (E(epsilon) = 0)

data_frame = pd.read_excel("Data_Linear.xlsx")
matrix_data = np.asarray(data_frame.astype(np.float64))
Y = matrix_data.T[0]

Z = np.zeros((len(matrix_data.T[0]), len(matrix_data.T)))
for i in range(len(Z)):
    Z[i][0] = 1

for row in range(len(Z)):
    for col in range(len(Z[0])-1):
        Z[row][col+1] = matrix_data[row][col+1]
print(Z)


# print(matrix_data.T[0])
# print(len(matrix_data.T))


