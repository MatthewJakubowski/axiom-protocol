import hashlib
from datetime import datetime

class DigitalManifest:
    def __init__(self, creator_id, content_hash):
        self.creator_id = creator_id
        self.timestamp = str(datetime.now())
        self.content_hash = content_hash
        # Symulacja podpisu cyfrowego
        self.signature = hashlib.sha256((content_hash + "PRIVATE_KEY").encode()).hexdigest()

def verify_content(media_data: str, manifest: DigitalManifest) -> bool:
    print(f"   [LOG] Sprawdzanie podpisu kryptograficznego C2PA...")
    current_hash = hashlib.sha256(media_data.encode()).hexdigest()
    
    if current_hash != manifest.content_hash:
        print("   [CRITICAL] BŁĄD: Suma kontrolna niezgodna (Deepfake).")
        return False
    
    expected_sig = hashlib.sha256((current_hash + "PRIVATE_KEY").encode()).hexdigest()
    if manifest.signature != expected_sig:
        print("   [CRITICAL] BŁĄD: Podpis cyfrowy sfałszowany.")
        return False
        
    print("   [OK] Materiał autentyczny.")
    return True
