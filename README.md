# Claim Estimator Tool

*Part of the PrimeFlex Claims Ecosystem*

---

## Overview

This tool applies public adjusting logic to property insurance claims. It calculates:

* Adjusted estimate totals including Overhead & Profit (O\&P)
* Deductibles
* Final payout to the policyholder

This script is designed to connect with Bubble.io (via API) or run standalone via terminal.

---

## Current Features

* Input: base estimate amount (manual or via JSON/API)
* Logic: adds 10% O\&P + 10% profit, subtracts deductible
* Output: formatted summary
* Loop mode: multiple estimates processed

---

## Example Output

```
Base Estimate: $14,000.00
O&P Applied: $2,940.00
Deductible: $1,000.00
Final Payout: $15,940.00
```

---

## Planned Features

* Export summary to .txt or PDF
* Bubble API connection
* Claim health scoring logic
* O\&P auto-justification rules

---

## How to Run (Basic Python)

```
python main.py
```

---

## License

Open source for educational and internal use under the PrimeFlex Adjusters brand.

---

**Jeremy Perry**
Founder, PrimeFlex Adjusters
Cincinnati, OH
*"Not just managing claims. Optimizing outcomes."*
