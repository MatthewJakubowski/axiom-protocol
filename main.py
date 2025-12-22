from src.reputation import AxiomNode, ReputationEngine, VerificationResult
from src.provenance import DigitalManifest, verify_content
from src.sybil import simulate_sybil_attack
import hashlib

def run_system():
    print("=== AXIOM PROTOCOL V1.0 (CONCEPT) ===")
    
    print("\n[MODUŁ 1] Ekonomia Prawdy")
    node = AxiomNode("Journalist_01")
    stake = ReputationEngine.calculate_stake(impact=5.0, confidence=0.9)
    ReputationEngine.process_verification(node, stake, VerificationResult.VERIFIED_TRUE)
    
    print("\n[MODUŁ 2] Ochrona C2PA")
    data = "Breaking News"
    manifest = DigitalManifest("Camera_Sony", hashlib.sha256(data.encode()).hexdigest())
    verify_content(data, manifest)
    
    print("\n[MODUŁ 3] Obrona Sybil")
    simulate_sybil_attack(20000.0)

if __name__ == "__main__":
    run_system()
