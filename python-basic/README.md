## Python Basic Operations

### Chart
```python
import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0,10) 
y = x ^ 2 
#Simple Plot
plt.plot(x,y)  

# save in pdf formats
plt.savefig('chart.pdf', format='pdf')
```