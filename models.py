from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Company:
    name: str
    description: str
    domain: str
    context: List[Dict[str, str]] = field(default_factory = list)
