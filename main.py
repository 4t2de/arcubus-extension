from data_loader import load_companies, load_questions
from engine import DiscoveryEngine

def run_discovery():
    domain_choice = input("Enter domain: (ex. Finance, Fintech): ").strip().lower()

    all_companies = load_companies(domain_choice)
    questions = load_questions(domain_choice)

    if not questions:
        print(f"No questions found in the domain: {domain_choice}")
        return

    engine = DiscoveryEngine(all_companies)

    for q in questions:
        print(f"\n[Question]: {q.text}")
        user_answer = input("Your answer: ")

        engine.filter_pool(q.text, user_answer)

        current_count = len(engine.get_results())
        print(f"Number of matches remaining: {current_count}")

        if current_count == 0:
            print("No companies match your requirements.")
            break
        if current_count == 1:
            break

    final_results = engine.get_results()
    print("Final Recommendations: ")
    if final_results:
        for company in final_results:
            print(f"{company.name}")
    else:
        print("No matching companies for your input.")

if __name__ == "__main__":
    run_discovery()
