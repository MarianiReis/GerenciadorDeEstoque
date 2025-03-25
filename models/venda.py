from dataclasses import dataclass
from typing import List

@dataclass
class Venda:
    id: int = None
    data: str = ""
    total: float = 0.0

@dataclass
class ItemVenda:
    id: int = None
    venda_id: int = None
    produto_id: int = None
    quantidade: int = 0