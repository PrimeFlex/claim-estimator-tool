def apply_op(base):
    base += base * 0.10  # Overhead
    base += base * 0.10  # Profit
    return base

summaries = []

# Ask for deductible once
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
        adjusted = apply_op(base_estimate)
        final_payout = adjusted - deductible

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
