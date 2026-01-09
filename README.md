## Architecture

* **Data (`/data`)**: CSV-based storage for Companies (Name, Description) and Questions.
* **Models (`models.py`)**: Data blueprints for Company and Question objects.
* **Loader (`data_loader.py`)**: Converts raw CSV rows into iterable Python objects.
* **Engine (`engine.py`)**: The filtering logic that evaluates matches between descriptions and user answers.
* **Main (`main.py`)**: The CLI orchestrator that manages the iterative loop.

## Logic

1. **Selection**: User picks a domain; the system loads targeted questions and the full company pool.
2. **The Sieve**: The Engine iterates through the pool, passing the **Company Description** and **User Answer** to a decision method.
3. **Reduction**: Only companies that satisfy the user's intent remain in the pool for the next question.
4. **Result**: A refined list of recommended companies is displayed.

## Future Integration

The `engine.py` is architected for a drop-in **LLM API** replacement. By inserting a Gemini or OpenAI call, the engine can implement to true semantic reasoning.

## Usage

1. Populate `data/companies.csv` and `data/questions.csv`.
2. Execute the discovery loop:
```bash
python main.py
```
