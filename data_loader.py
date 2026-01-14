import csv
from models import Company

def load_companies(domain_filter, path="data/companies.csv"):
    companies = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['domain'].lower() == domain_filter.lower():
                companies.append(Company(
                    name=row['name'],
                    description=row['description'],
                    domain=row['domain']
                ))
    return companies
