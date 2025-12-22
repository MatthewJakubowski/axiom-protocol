def simulate_sybil_attack(budget: float):
    ENTRY_COST = 110.0 
    print(f"   [LOG] Atakujący z budżetem ${budget} próbuje przejąć sieć...")
    
    bots_possible = int(budget // ENTRY_COST)
    print(f"   [ANALIZA] Atakujący może stworzyć maksymalnie {bots_possible} botów.")
    
    if bots_possible > 5000:
        print("   [FAIL] UWAGA: Atakujący przejął sieć!")
    else:
        print("   [DEFENSE] System bezpieczny. Atakujący zbankrutował.")
