## Architecture

* **Data `/data`**: CSV-based storage for Companies (Name, Description) and Questions.
* **Models `models.py`**: Data blueprints for Company and Question objects.
* **Loader `data_loader.py`**: Converts raw CSV rows into iterable Python objects.
* **Engine `engine.py`**: The filtering logic that evaluates matches between descriptions and user answers.
* **Main `main.py`**: The CLI orchestrator that manages the iterative loop.

## Logic

1. This system is to be used top of the existing Arcubus application, which is primarily used to scrape company websites and extract description summaries.
2. Firstly, the user is asked for the domain. The search space (or more like the filter space) is reduced to only the companies in that given domain.
3. Subsequent questions are asked. The company details for comparison can be added into the `companies.csv` file.
4. Questions can be added regarding your usage in the `questions.csv` file.
5. For each question, the question content, the user answer is given as prompt for each company to determine if the given company suits the comparison or not.
6. The search space (or rather the filter space) is reduced with each given question, and the loop terminates when there are no companies remaining which fit the criteria, or only 1 company remains (which is then returned as result).

## Future Integration

Context Graph/GraphRAG integration to further improve the LLM performance.

## Usage

1. Populate `data/companies.csv` and `data/questions.csv`.
2. Execute the discovery loop:
```python
python main.py
```
