from dataclasses import dataclass

@dataclass
class Company:
    name: str
    description: str
    domain: str

@dataclass
class Question:
    domain: str
    text: str
