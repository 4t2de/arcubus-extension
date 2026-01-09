import os
import csv

# Create the data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

# Create companies.csv
companies = [
    ["name", "description"],
    ["AlphaBank", "A traditional commercial bank focusing on high-interest savings and corporate lending."],
    ["QuickPay", "A fintech startup providing mobile-first payment solutions for freelancers and small vendors."],
    ["BlockChainLedger", "A B2B financial tech company specializing in distributed ledger technology for international settlements."],
    ["SafeVault", "Secure personal banking app for consumer savings and micro-investing."],
    ["TradeFlow", "An enterprise platform for global supply chain financing and B2B payments."]
]

with open('data/companies.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(companies)

# Create questions.csv
questions = [
    ["domain", "text"],
    ["finance", "Are you looking for personal banking or corporate lending?"],
    ["finance", "Do you require high-interest savings accounts?"],
    ["fintech", "Do you prefer mobile-first apps or desktop enterprise platforms?"],
    ["fintech", "Are you interested in blockchain or distributed ledger technology?"],
    ["fintech", "Is your focus on B2B payments or consumer spending?"]
]

with open('data/questions.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(questions)

print("Data folder and CSV files created successfully!")
