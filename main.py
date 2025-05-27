# main.py
from payout import calculate_payout

summaries = []

try:
    deductible_input = input("Enter deductible amount: $")
    deductible = float(deductible_input)
except ValueError:
    print("Invalid deductible. Using default of $1,000.")
    deductible = 1000

while True:
    user_input = input("Enter base estimate amount (or type 'done' to finish): ")

    if user_input.lower() == "done":
        print("\n--- Claim Summary Report ---")
        for s in summaries:
            print(s)
        print("\nAll claims processed.")
        break

    try:
        base_estimate = float(user_input)
        final_payout, adjusted = calculate_payout(base_estimate, deductible)

        summary = (
            f"Estimate: ${base_estimate:,.2f} | "
            f"O&P Total: ${adjusted:,.2f} | "
            f"Deductible: ${deductible:,.2f} | "
            f"Final Payout: ${final_payout:,.2f}"
        )

        summaries.append(summary)

        print("\n" + summary + "\n" + "-" * 40)

    except ValueError:
        print("Please enter a valid number or type 'done'.")
