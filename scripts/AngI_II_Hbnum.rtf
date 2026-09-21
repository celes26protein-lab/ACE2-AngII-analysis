import pandas as pd

def read_hbond(filename):
    vals = []

    with open(filename) as f:
        for line in f:
            if line.startswith('#') or line.startswith('@'):
                continue

            vals.append(float(line.split()[1]))

    return pd.Series(vals)

angI = read_hbond("AngI_hbnum.xvg")
angII = read_hbond("AngII_hbnum.xvg")

print("AngI")
print("mean =", angI.mean())
print("std  =", angI.std())

print()

print("AngII")
print("mean =", angII.mean())
print("std  =", angII.std())

from scipy.stats import ttest_ind

t, p = ttest_ind(
    angI,
    angII,
    equal_var=False
)

print("t =", t)
print("p =", p)
