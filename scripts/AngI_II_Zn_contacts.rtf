import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#.xvg libraries
def read_xvg(filename):
    data = []
    with open(filename) as f:
        for line in f:
            if line.startswith(("@", "#")):
                continue
            cols = line.split()
            data.append([float(x) for x in cols])
    return np.array(data)

#data analysis
angI = read_xvg("contact_AngI.xvg")
angII = read_xvg("contact_AngII.xvg")

t_I = angI[:, 0]
c_I = angI[:, 1]

t_II = angII[:, 0]
c_II = angII[:, 1]

#Average
print("AngI mean contact:", np.mean(c_I))
print("AngII mean contact:", np.mean(c_II))

print("AngI occupancy (%):", np.mean(c_I > 0) * 100)
print("AngII occupancy (%):", np.mean(c_II > 0) * 100)

#t-test
tstat, pval = stats.ttest_ind(c_I, c_II, equal_var=False)

print("t-stat:", tstat)
print("p-value:", pval)

#plott, graph
plt.figure()

plt.plot(t_I, c_I, label="AngI")
plt.plot(t_II, c_II, label="AngII")

plt.xlabel("Time (ps)")
plt.ylabel("Contacts")
plt.legend()
plt.title("ACE2–Ligand Contact")

plt.show()

#comparision
plt.figure()

plt.hist(c_I, bins=30, alpha=0.5, label="AngI")
plt.hist(c_II, bins=30, alpha=0.5, label="AngII")

plt.legend()
plt.title("Contact distribution")
plt.show()
