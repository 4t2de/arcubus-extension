import csv
from models import Company, Question

def load_companies(path="data/companies.csv"):
    companies = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            companies.append(Company(name = row['name'], description = row['description']))
    return companies

def load_questions(path = "data/questions.csv"):
    questions = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            questions.append(Question(domain = row['domain'], text = row['text']))
    return questions
