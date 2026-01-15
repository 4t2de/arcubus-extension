## Architecture

* **Data `/data`**: CSV-based storage for Companies (Name, Description, Domain) only. Removed questions in this revision.
* **Models `models.py`**: Data blueprints for Company objects.
* **Loader `data_loader.py`**: Converts raw CSV rows into iterable Python objects.
* **Engine `engine.py`**: Processing logic.
* **Main `main.py`**: Main orchestrator.

## Logic

This is the third revised version, and the working has been changed.
Earlier:
1. Questions were hardcoded in a .csv file, so that the user can tune questions per their need.
2. Once the domain was selected, the operations were only performed on the companies with similar domain (which is still the case).
3. Earlier, the architecture was a loop of user-coded question with user answers, which were sent to the LLM to further reduce the pool of companies for comparison.
4. The output was a list of companies which still match the user description/need.

Current:
1. `questions.csv` is completely removed. The questions are now LLM generated.
2. The input format has been changed. After selecting the domain, now a company is selected for the deep dive.
3. Once the company is selected, the LLM is fed with the company description which is previously scraped, and a vague question is asked in order to understand the aspects on the basis of which the user wants to perform a deep dive.
4. 4 questions are asked in order to clearly understand the user's criteria for analysis. For each question asked, the question text, the user's answer are appended into the LLM prompt in order to add context retention (since LLMs cannot retain context over API calls).
5. The output now is the collated answers over different subsequent questions (final deep dive) on the selected company on the aspects that user defines.

## Future Integration

Context Graph/GraphRAG integration to further improve the LLM performance.

## Usage

1. Populate `data/companies.csv` (using Arcubus).
2. Execute the discovery loop:
```bash
python main.py
```
