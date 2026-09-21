# ACE2–Angiotensin MD Trajectory Analysis

Analysis of the GROMACS MD trajectories for the ACE2–Ang I and ACE2–Ang II
complexes (see
[ACE2-AngII-GROMACS](https://github.com/https://github.com/celes26protein-lab/ACE2-AngII-GROMACS)),
as described in our published paper (see [Citation](#citation)).

This repository is part of a linked series:

1. [ACE2-AngII-structures](https://github.com/https://github.com/celes26protein-lab/ACE2-AngII-structures) — receptor/ligand structures (incl. raw NeuroSnap output)
2. [ACE2-AngII-smina-docking](https://github.com/https://github.com/celes26protein-lab/ACE2-AngII-smina-docking) — docking runs and results
3. [ACE2-AngII-GROMACS](https://github.com/https://github.com/celes26protein-lab/ACE2-AngII-GROMACS) — MD simulation
4. **ACE2-AngII-analysis** (this repository) — trajectory analysis

## Contents

```
xvg/         # GROMACS analysis output (.xvg) — e.g. RMSD, RMSF, H-bonds, distance to Zn²⁺
scripts/     # Python analysis/plotting scripts (developed in PyCharm)
results/     # Compiled result figures/PDF
```

## Method

GROMACS trajectory analysis tools were used to generate `.xvg` output
(e.g. RMSD, RMSF, hydrogen-bond occupancy, distance between each peptide
and the catalytic Zn²⁺ ion) from the production MD runs in
[ACE2-AngII-GROMACS](https://github.com/https://github.com/celes26protein-lab/ACE2-AngII-GROMACS).
These outputs were further processed and plotted using the Python scripts
in `scripts/`.

<!-- Add a short description of each script and what each result figure shows once the files are added, e.g.:
- `scripts/plot_rmsd.py` — plots backbone RMSD over the simulation for both complexes
-->

## Quantitative Results

### Zn²⁺–Peptide Distance

![Zn-peptide distance vs time and distribution](results/zn_peptide_distance.png)

Docking predicted a shorter Zn–ligand distance for Ang II (2.3 Å) than
Ang I (4.1 Å). MD-derived minimum Zn–peptide distances over the 1 ns
trajectory:

| Peptide | Mean ± SD | 
|---|---|
| Ang I  | 26.27 ± 0.51 Å |
| Ang II | 24.62 ± 0.50 Å |

Welch's t-test: t = 23.1627, p = 1.7037e-58
ANOVA: F = 536.5113, p = 1.5994e-58

Ang II maintained a consistently shorter distance to the catalytic Zn²⁺
throughout the trajectory, and its distribution of minimum distances is
shifted toward shorter values compared with Ang I.

### ACE2–Peptide Contact Number

![ACE2-ligand contact over time and distribution](results/ace2_ligand_contact.png)

| Peptide | Mean contacts | Occupancy |
|---|---|---|
| Ang I  | 3059.48 | 100.0% |
| Ang II | 2669.88 | 100.0% |

t = 21.1142, p = 8.3872e-53

Ang I maintains a larger contact interface with ACE2 than Ang II
throughout the trajectory, and the difference is highly significant. Both
peptides remain in continuous contact (100% occupancy), so the difference
lies in contact *extent*, not binding/unbinding events.

### Hydrogen-Bond Occupancy

| Peptide | Mean | SD |
|---|---|---|
| Ang I  | 5.574 | 0.898 |
| Ang II | 5.149 | 0.876 |

t = 3.4097, p = 0.000787 (Ang I > Ang II)

### Active-Site Distance (contact defined as < 4.0 Å)

| Peptide | Mean ± SD | Contact occupancy (< 4.0 Å) |
|---|---|---|
| Ang I  | 17.32 ± 0.44 Å | 0.0% |
| Ang II | 17.11 ± 0.35 Å | 0.0% |

t = 3.7730, p = 2.1563e-04
F = 1.6266, F-test p = 1.5754e-02

> **Note:** the three distance metrics above (SMINA docking Zn distance:
> 2–4 Å; MD minimum Zn–peptide distance: ~24–27 Å; MD active-site
> distance: ~17 Å) are on very different scales, most likely because each
> measures a different reference point (e.g. closest heavy atom to the Zn²⁺
> ion vs. a peptide center-of-mass/active-site-pocket definition). Worth
> double-checking that the same definition is used consistently, or
> stating each definition explicitly, before finalizing the manuscript
> figures.

## Summary of Findings

**Ang I**
- Better docking score
- More protein contacts
- More hydrogen bonds
- Larger interaction interface

This suggests stronger overall association with ACE2.

**Ang II**
- Closer to catalytic Zn²⁺ in the docking pose
- Remains closer to Zn²⁺ throughout MD
- More effective competitor in enzyme assays

## Discussion

Docking simulations predicted a more favorable binding affinity for Ang I
than for Ang II (−8.5 vs −7.4 kcal/mol), accompanied by a larger ACE2
contact interface and slightly higher hydrogen-bond occupancy during MD
simulations. These findings suggest that Ang I establishes more extensive
overall interactions with ACE2. However, Ang II consistently remained
closer to the catalytic Zn²⁺ ion, both in the initial docking pose (2.3 Å
versus 4.1 Å for Ang I) and throughout the MD trajectory. This trend is
consistent with the experimental competition assay, in which Ang II
reduced ACE2 activity more effectively than Ang I at the same
concentration.

Although Ang I exhibited a more favorable docking score and formed a
larger interaction network with ACE2, these interactions do not
necessarily translate into effective access to the catalytic center. In
contrast, the consistently shorter Zn²⁺–peptide distances observed for
Ang II suggest a binding mode that is more closely associated with the
catalytic machinery. Thus, while Ang I may engage ACE2 more extensively,
Ang II appears to adopt a more catalytically relevant binding orientation,
enabling more effective competition with substrate processing and
resulting in stronger inhibition of ACE2 activity.

## Interpretation: Contact Extent vs. Catalytic-Site Engagement

Contact number from MD reflects surface adhesion, conformational
complementarity, and diffuse contact area — it is a measure of how
broadly a peptide sits on the protein surface, not a direct proxy for
enzymatic parameters such as K_m or k_cat. It is therefore possible for
Ang II to be functionally more important at the catalytic site while
still showing a lower raw contact count than Ang I.

Two binding modes are consistent with the data:

- **Ang I — broad, shallow engagement.** As a longer, more flexible
  peptide, Ang I may spread across a wider surface area, increasing its
  contact count and H-bond count without necessarily binding more
  tightly at any single site. This looks like "more contact," not
  "stronger binding."
- **Ang II — narrow, deep engagement.** Despite fewer total contacts,
  Ang II consistently sits closer to the catalytic Zn²⁺ and may rely on
  a smaller number of specific, high-value interactions (e.g. salt
  bridges or key hydrogen bonds) at the catalytic position. Contact
  count alone would not capture this.

This reconciles an apparent tension with prior biological understanding
(Ang II is generally considered the principal ACE2 substrate), and with
the experimental competition assay, where Ang II inhibits ACE2 activity
more effectively than Ang I:

| Metric | Ang I | Ang II |
|---|---|---|
| Contact interface (MD) | Larger | Smaller |
| Binding specificity | Likely lower | Likely higher |
| Active-site engagement | Weaker | Stronger |
| Competitive inhibition (experimental) | Weaker | Stronger |

In short, the MD contact-number metric captures *how broadly* a peptide
contacts ACE2, not *how specifically or catalytically relevant* that
contact is. The higher Ang I contact count should be reported as "a more
extensive contact interface," not interpreted as "stronger binding to
the catalytic site" — the latter is better supported by the Zn²⁺-distance
and experimental inhibition data, which both favor Ang II.

## Requirements

- Python (see `scripts/` for specific package requirements, e.g. `numpy`, `pandas`, `matplotlib`)

## Citation

Suzuki YJ, Tamazawa Y, Bablu FE, Gonzales ES, Ghafoor TS, Chung CS,
Suzuki AM, Mickelson AR, Murphy EJ, Hao J, Teramoto T. Structural and
functional significance of arginine at position 2 of angiotensin II:
Implications for oxidant-mediated amino acid residue conversions.
*Free Radical Biology and Medicine* (2026).
DOI: [10.1016/j.freeradbiomed.2026.09.015](https://doi.org/10.1016/j.freeradbiomed.2026.09.015)

## License

[MIT License](LICENSE)