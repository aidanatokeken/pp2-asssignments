import re
import json

# Read receipt text
with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 1. Extract all prices
price_pattern = r"\d[\d\s]*,\d{2}"
prices = re.findall(price_pattern, text)

# Convert prices to float
prices_clean = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

# 2. Extract product names
product_pattern = r"\d+\.\n(.+)"
products = re.findall(product_pattern, text)

# Clean product names
products = [p.strip() for p in products]

# 3. Calculate total amount (sum of product prices)
total = sum(prices_clean)

# 4. Extract date and time
datetime_pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}"
datetime_match = re.search(datetime_pattern, text)
datetime_value = datetime_match.group() if datetime_match else None

# 5. Find payment method
payment_pattern = r"(Банковская карта|Наличные)"
payment_match = re.search(payment_pattern, text)
payment_method = payment_match.group() if payment_match else "Unknown"

# 6. Structured output
data = {
    "products": products,
    "prices": prices_clean,
    "calculated_total": total,
    "date_time": datetime_value,
    "payment_method": payment_method
}

print(json.dumps(data, indent=4, ensure_ascii=False))