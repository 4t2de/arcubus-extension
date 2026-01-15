from data_loader import load_companies
from engine import AnalysisEngine

def run_discovery():
    domain_choice = input("Enter domain: (ex. Finance, Fintech): ").strip().lower()
    companies = load_companies(domain_choice)
    if not companies:
        print(f"No companies found in the domain: {domain_choice}")
        return
    print(f"\nCompanies available in {domain_choice}:")
    for c in companies:
        print(f"- {c.name}")

    target_name = input("\nPlease enter the company you want to analyze (case sensitive): ").strip()
    target_company = next((c for c in companies if c.name == target_name), None)
    if not target_company:
        print(f"Error: Company '{target_name}' not found in the {domain_choice} list.")
        return

    print(f"\nStarting analysis for: {target_company.name}")

    engine = AnalysisEngine()

    user_input = None

    for i in range(4):
        question = engine.get_next_question(target_company, user_input)
        print(f"\n[AI]: {question}")
        user_input = input("Your answer: ")

    print("Generating final summary: ")

    report = engine.get_final_summary(target_company)
    print(report)

if __name__ == "__main__":
    run_discovery()
