from scipy.stats import binomtest


primary = {"tn": 26831, "fp": 10169, "fn": 713, "tp": 44619}
conservative = {"tn": 30176, "fp": 6824, "fn": 1800, "tp": 43532}

false_positives_corrected = primary["fp"] - conservative["fp"]
true_positives_lost = primary["tp"] - conservative["tp"]
primary_errors = primary["fp"] + primary["fn"]
conservative_errors = conservative["fp"] + conservative["fn"]
net_correct_gain = primary_errors - conservative_errors
error_reduction_percent = 100 * net_correct_gain / primary_errors
fp_avoided_per_additional_miss = false_positives_corrected / true_positives_lost

# Raising the threshold creates two paired discordant correctness counts:
# former false positives corrected, and former true positives lost.
mcnemar = binomtest(
    min(false_positives_corrected, true_positives_lost),
    n=false_positives_corrected + true_positives_lost,
    p=0.5,
    alternative="two-sided",
)

print(f"False positives corrected: {false_positives_corrected}")
print(f"True positives lost: {true_positives_lost}")
print(f"Net additional correct decisions: {net_correct_gain}")
print(f"Total error reduction: {error_reduction_percent:.2f}%")
print(
    "False positives avoided per additional missed attack: "
    f"{fp_avoided_per_additional_miss:.2f}"
)
print(f"Exact two-sided McNemar p-value: {mcnemar.pvalue:.6e}")

assert false_positives_corrected == 3345
assert true_positives_lost == 1087
assert net_correct_gain == 2258
assert round(error_reduction_percent, 2) == 20.75
assert round(fp_avoided_per_additional_miss, 2) == 3.08
