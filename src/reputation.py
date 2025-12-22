import math
from enum import Enum
from dataclasses import dataclass

class VerificationResult(Enum):
    VERIFIED_TRUE = "TRUE"
    VERIFIED_FALSE = "FALSE"

@dataclass
class AxiomNode:
    node_id: str
    reputation: float = 100.0
    
    def get_max_stake(self) -> float:
        return self.reputation * 0.5

class ReputationEngine:
    @staticmethod
    def calculate_stake(impact: float, confidence: float) -> float:
        # Symulacja algorytmu wyceny ryzyka
        base_cost = 10.0
        risk_multiplier = math.exp(impact * 0.25) 
        return round(base_cost * risk_multiplier * (1 / confidence), 2)

    @staticmethod
    def process_verification(node: AxiomNode, stake: float, result: VerificationResult):
        print(f"   [LOG] Weryfikacja węzła {node.node_id}...")
        if result == VerificationResult.VERIFIED_TRUE:
            reward = stake * 0.8
            node.reputation += reward
            print(f"   [SUCCESS] Wynik: PRAWDA. Nowa reputacja: {node.reputation:.2f}")
        elif result == VerificationResult.VERIFIED_FALSE:
            penalty = stake * 2.5
            node.reputation -= penalty
            if node.reputation < 0: node.reputation = 0
            print(f"   [SLASHED] Wynik: KŁAMSTWO. Nowa reputacja: {node.reputation:.2f}")
