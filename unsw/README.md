# UNSW-NB15 Summary-Level Verification Package

This directory records the aggregate outcomes reported for the official UNSW-NB15 partition and the development-selected conservative operating point.

## Included

- The original and conservative holdout confusion matrices.
- Aggregate metrics and reported confidence intervals.
- The five-seed mean and standard deviation summary.
- The two available category endpoints: Normal specificity and Fuzzers recall.
- A script that recomputes the net error reduction, false-positive-to-missed-attack trade-off, and exact two-sided McNemar p-value from the paired discordant counts.

## Boundary

This is not a full row-level reproduction archive. The source UNSW-NB15 records and row-level holdout predictions are not included. Consequently, users can verify the arithmetic of the reported operating-point comparison but cannot independently reconstruct all confidence intervals or every per-category metric from this directory alone.

No missing category values are inferred. The repository reports only category results preserved in the experiment record.
