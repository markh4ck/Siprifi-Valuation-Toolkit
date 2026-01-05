# Startup Valuation Tool
# Methods: First Chicago, Certainty Equivalent, Discounted Rate with CAPM

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display



# -----------------------
# 1. INPUTS
# -----------------------
cash_flows = {
    'year': [1, 2, 3, 4, 5],
    'base': [100000, 150000, 200000, 250000, 300000],
    'best': [120000, 180000, 240000, 300000, 360000],
    'worst': [80000, 120000, 160000, 200000, 240000]
}

probabilities = {'best': 0.2, 'base': 0.5, 'worst': 0.3}

rf = 0.03     # Risk-free rate
beta = 1.2    # Beta of startup
rm = 0.08     # Expected market return

risk_adjustment = {'year1':0.9, 'year2':0.85, 'year3':0.8, 'year4':0.75, 'year5':0.7}

df = pd.DataFrame(cash_flows)

# -----------------------
# 2. DISCOUNT RATE (CAPM)
# -----------------------
discount_rate = rf + beta * (rm - rf)
print(f"Discount rate (CAPM): {discount_rate:.2%}\n")

# -----------------------
# 3. NPV FUNCTION
# -----------------------
def npv(rate, cashflows):
    return sum(cf / (1 + rate)**i for i, cf in enumerate(cashflows, start=1))

# -----------------------
# 4. FIRST CHICAGO METHOD
# -----------------------
npv_best = npv(discount_rate, df['best'])
npv_base = npv(discount_rate, df['base'])
npv_worst = npv(discount_rate, df['worst'])

first_chicago_value = (probabilities['best']*npv_best +
                       probabilities['base']*npv_base +
                       probabilities['worst']*npv_worst)

print(f"First Chicago Valuation: ${first_chicago_value:,.0f}\n")

# -----------------------
# 5. CERTAINTY EQUIVALENT METHOD
# -----------------------
ce_cashflows = [cf * risk_adjustment[f'year{i+1}'] for i, cf in enumerate(df['base'])]
ce_value = npv(rf, ce_cashflows)
print(f"Certainty Equivalent Valuation: ${ce_value:,.0f}\n")

# -----------------------
# 6. DISPLAY TABLE
# -----------------------
print("Projected Cash Flows Table:")
print(df.to_string(index=False))

# -----------------------
# 7. VISUALIZATION
# -----------------------
sns.set_style("whitegrid")

# Cash flows over time
plt.figure(figsize=(10,6))
plt.plot(df['year'], df['best'], label='Best Case', marker='o', color='green')
plt.plot(df['year'], df['base'], label='Base Case', marker='o', color='blue')
plt.plot(df['year'], df['worst'], label='Worst Case', marker='o', color='red')
plt.title('Projected Cash Flows')
plt.xlabel('Year')
plt.ylabel('Cash Flow ($)')
plt.legend()
plt.show()

# NPV by scenario
plt.figure(figsize=(6,4))
plt.bar(probabilities.keys(), [npv_best, npv_base, npv_worst], color=['green','blue','red'])
plt.ylabel('NPV ($)')
plt.title('NPV by Scenario')
plt.show()

# Certainty Equivalent cash flows
plt.figure(figsize=(10,6))
plt.plot(df['year'], ce_cashflows, label='Certainty-Equivalent Cash Flows', marker='o', color='purple')
plt.title('Certainty-Equivalent Cash Flows')
plt.xlabel('Year')
plt.ylabel('Cash Flow ($)')
plt.legend()
plt.show()

# -----------------------
# 8. SUMMARY
# -----------------------
summary = pd.DataFrame({
    'Method': ['First Chicago', 'Certainty Equivalent'],
    'Valuation ($)': [first_chicago_value, ce_value]
})
print("Summary Valuation:")
display(summary)
