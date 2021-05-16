from matplotlib import colors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pf= pd.read_csv("Car_sales.csv")
print(pf.head(20))
grouped = pf.groupby('Manufacturer')
print(grouped['Sales_in_thousands'].agg([np.sum]))
data = pf[pf['Manufacturer'] == 'Chevrolet']
data1 = data["Model"]
plt.title("Biểu đồ phân bố của hãng Chevrolet")
plt.xlabel("MODEL")
plt.ylabel("Sales_in_thousands")
plt.bar(data1, data["Sales_in_thousands"],color="pink",width=0.5)
plt.show()