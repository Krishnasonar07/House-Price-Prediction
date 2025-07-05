import numpy as np
np.set_printoptions(suppress=True)
A = np.loadtxt('d:/programs/PYTHON/Housing.csv', delimiter=',')
Y = (np.loadtxt('d:/programs/PYTHON/price.csv',delimiter=','))
B = (np.linalg.inv((A.T@A))@(A.T@Y))
sum=0
diff =Y-(A@B)
for i in range(Y.shape[0]):
    sum += abs(diff[i,]/Y[i,])
map = (sum*100)/545
# rmse = np.sqrt(np.sum((Y-(A@B)),axis=0)/545)
predicted=A@B
np.savetxt('d:/programs/PYTHON/predicted_prices.csv', predicted, delimiter=',', header='PredictedPrice', comments='', fmt='%.2f')
print(map)
# print(B.shape)
# print(Y.shape)