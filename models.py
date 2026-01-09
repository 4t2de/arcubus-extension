from dataclasses import dataclass

@dataclass
class Company:
    name: str
    description: str

@dataclass
class Question:
    domain: str
    text: str
