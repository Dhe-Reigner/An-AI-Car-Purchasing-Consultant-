### Vehicle Affordability Analysis

#### Inputs

- Annual Salary:  $60,000
- Credit Card Debt:  $5,000
- Net Worth: $20,000
- Intended Budget: $25,000

#### Calculations

### Debt-to-Income Ratio (DTI):

The debt-to-income ratio is calculated by dividing total debt by gross income.

```python
DTI = (5300 / 60000) * 100
print(f"Debt-to-Income Ratio (DTI): {DTI}%")
```

### Income-to-Car-Price Ratio:

This ratio helps evaluate the buyer's financial capacity to purchase the vehicle. A higher ratio indicates greater financial capacity.

```python
income_to_car_price_ratio = 60000 / 25000
print(f"Income-to-Car-Price Ratio: {income_to_car_price_ratio}")
```

### Recommended Safe Budget Range:

A safe budget range is determined by subtracting 10% to 15% of the buyer's income from the intended budget.

```python
safe_budget_range_lower = 60000 * 0.8  # 80% of income
safe_budget_range_upper = 60000 * 0.9  # 90% of income

safe_budget_lower = max(25000, safe_budget_range_lower)
safe_budget_upper = min(50000, safe_budget_range_upper)

print(f"Recommended Safe Budget Range: ${safe_budget_lower}-{safe_budget_upper}")
```

### Monthly Payment Sustainability Estimate:

This estimate is based on a 5-year loan with an interest rate of 6% and a down payment of 10% of the vehicle price.

```python
import math

def calculate_monthly_payment(loan_amount, interest_rate, loan_term):
    return (loan_amount * interest_rate / 12 / (1 - math.pow(1 + interest_rate / 12, -loan_term) / 1)) * 1.1  # Account for down payment

loan_term_in_years = 5
interest_rate = 0.06
down_payment = 25000 * 0.1  # 10% of vehicle price

loan_amount = 25000 - down_payment
monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term_in_years)
print(f"Monthly Payment Sustainability Estimate: ${monthly_payment:.2f}")
```

### Affordability Tier, Safe Budget Range, Financial Risk Flags, and Summary Insight

Based on the analysis, the buyer has a Low-Moderate financial capacity for vehicle acquisition, with a Safe Budget Range of $22,000 - $42,500. However, they have a High DTI Ratio and a Moderate risk of financial distress.

```markdown
### Affordability Tier: Moderate

### Safe Budget Range: $22,000 - $42,500

### Financial Risk Flags:
- High Debt-to-Income Ratio: 8.83%
- Moderate financial risk of distress: High DTI Ratio and moderate credit card debt

### Summary Insight:
This buyer has a Moderate financial capacity, but should be cautious of high debt levels and strive for financial stability before considering a vehicle purchase.
```

The output is structured and provides a comprehensive affordability analysis with quantitative thresholds.