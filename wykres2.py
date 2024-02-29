import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(0, 1, 1000)

plt.hist(data, bins=30)
plt.title("Histogram")
plt.xlabel("Wartości")
plt.ylabel("Czstość")

plt.savefig("histogram.png")
plt.savefig("histogram.pdf")
plt.show()
