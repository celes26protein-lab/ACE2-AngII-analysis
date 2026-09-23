import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def read_xvg(filename):
    """
    Read GROMACS .xvg file
    """
    x = []
    y = []

    with open(filename) as f:
        for line in f:
            if line.startswith('#') or line.startswith('@'):
                continue

            cols = line.split()

            if len(cols) >= 2:
                x.append(float(cols[0]))
                y.append(float(cols[1]))

    return pd.DataFrame({
        "time_ps": x,
        "distance_nm": y
    })


# ==========================
# Load data
# ==========================

angI = read_xvg("Zn_AngI.xvg")
angII = read_xvg("Zn_AngII.xvg")

# convert nm -> Å
angI_dist = angI["distance_nm"] * 10
angII_dist = angII["distance_nm"] * 10


# ==========================
# Statistics
# ==========================

mean_I = angI_dist.mean()
std_I = angI_dist.std()

mean_II = angII_dist.mean()
std_II = angII_dist.std()

# Welch t-test
t_stat, p_value = stats.ttest_ind(
    angI_dist,
    angII_dist,
    equal_var=False
)

# ANOVA
F_value, p_anova = stats.f_oneway(
    angI_dist,
    angII_dist
)

print("=" * 50)
print("Zn-Peptide Distance Analysis")
print("=" * 50)

print(f"AngI  : {mean_I:.2f} ± {std_I:.2f} Å")
print(f"AngII : {mean_II:.2f} ± {std_II:.2f} Å")

print()
print(f"Welch t-test")
print(f"t = {t_stat:.4f}")
print(f"p = {p_value:.4e}")

print()
print(f"ANOVA")
print(f"F = {F_value:.4f}")
print(f"p = {p_anova:.4e}")

print("=" * 50)


# ==========================
# Time Series Plot
# ==========================

plt.figure(figsize=(8, 5))

plt.plot(
    angI["time_ps"] / 1000,
    angI_dist,
    label="AngI"
)

plt.plot(
    angII["time_ps"] / 1000,
    angII_dist,
    label="AngII"
)

plt.xlabel("Time (ns)")
plt.ylabel("Zn-peptide minimum distance (Å)")
plt.title("Zn-Peptide Distance vs Time")

plt.legend()

plt.tight_layout()

plt.savefig(
    "Zn_distance_timeseries.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================
# Histogram
# ==========================

plt.figure(figsize=(7, 5))

plt.hist(
    angI_dist,
    bins=30,
    alpha=0.6,
    label="AngI"
)

plt.hist(
    angII_dist,
    bins=30,
    alpha=0.6,
    label="AngII"
)

plt.xlabel("Zn-peptide minimum distance (Å)")
plt.ylabel("Counts")

plt.title("Distribution of Zn-Peptide Distances")

plt.legend()

plt.tight_layout()

plt.savefig(
    "Zn_distance_histogram.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================
# Bar Plot (Mean ± SD)
# ==========================

plt.figure(figsize=(5, 5))

means = [mean_I, mean_II]
stds = [std_I, std_II]

plt.bar(
    ["AngI", "AngII"],
    means,
    yerr=stds,
    capsize=5
)

plt.ylabel("Zn-peptide distance (Å)")
plt.title("Mean Zn-Peptide Distance")

plt.text(
    0.5,
    max(means) + max(stds) + 0.5,
    f"p = {p_value:.2e}\nF = {F_value:.2f}",
    ha="center"
)

plt.tight_layout()

plt.savefig(
    "Zn_distance_barplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
