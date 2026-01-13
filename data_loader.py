import csv
from models import Company, Question

def load_companies(domain_filter, path="data/companies.csv"):
    companies = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['domain'].lower() == domain_filter.lower():
                companies.append(Company(
                    name=row['name'],
                    description=row['description'],
                    domain=row['domain'] # Pass the new field here
                ))
    return companies

def load_questions(domain, path="data/questions.csv"):
    questions = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['domain'].lower() == domain.lower():
                questions.append(Question(domain=row['domain'], text=row['text']))
    return questions
