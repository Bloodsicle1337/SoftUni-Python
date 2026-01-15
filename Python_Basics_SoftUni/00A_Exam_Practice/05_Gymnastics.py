RUSSIA_RIBBON_DIFFICULTY = 9.100
RUSSIA_RIBBON_EXECUTION = 9.400
RUSSIA_HOOP_DIFFICULTY = 9.300
RUSSIA_HOOP_EXECUTION = 9.800
RUSSIA_ROPE_DIFFICULTY = 9.600
RUSSIA_ROPE_EXECUTION = 9.000

BULGARIA_RIBBON_DIFFICULTY = 9.600
BULGARIA_RIBBON_EXECUTION = 9.400
BULGARIA_HOOP_DIFFICULTY = 9.550
BULGARIA_HOOP_EXECUTION = 9.750
BULGARIA_ROPE_DIFFICULTY = 9.500
BULGARIA_ROPE_EXECUTION = 9.400

ITALY_RIBBON_DIFFICULTY = 9.200
ITALY_RIBBON_EXECUTION = 9.500
ITALY_HOOP_DIFFICULTY = 9.450
ITALY_HOOP_EXECUTION = 9.350
ITALY_ROPE_DIFFICULTY = 9.700
ITALY_ROPE_EXECUTION = 9.150

russia_ribbon_score = RUSSIA_RIBBON_DIFFICULTY + RUSSIA_RIBBON_EXECUTION
russia_hoop_score = RUSSIA_HOOP_DIFFICULTY + RUSSIA_HOOP_EXECUTION
russia_rope_score = RUSSIA_ROPE_DIFFICULTY + RUSSIA_ROPE_EXECUTION

bulgaria_ribbon_score = BULGARIA_RIBBON_DIFFICULTY + BULGARIA_RIBBON_EXECUTION
bulgaria_hoop_score = BULGARIA_HOOP_DIFFICULTY + BULGARIA_HOOP_EXECUTION
bulgaria_rope_score = BULGARIA_ROPE_DIFFICULTY + BULGARIA_ROPE_EXECUTION

italy_ribbon_score = ITALY_RIBBON_DIFFICULTY + ITALY_RIBBON_EXECUTION
italy_hoop_score = ITALY_HOOP_DIFFICULTY + ITALY_HOOP_EXECUTION
italy_rope_score = ITALY_ROPE_DIFFICULTY + ITALY_ROPE_EXECUTION

missing_rribbon = ((20 - russia_ribbon_score) / 20 ) * 100
missing_rhoop = ((20 - russia_hoop_score) / 20 ) * 100
missing_rrope = ((20 - russia_rope_score) / 20 ) * 100

missing_bribbon = ((20 - bulgaria_ribbon_score) / 20 ) * 100
missing_bhoop = ((20 - bulgaria_hoop_score) / 20 ) * 100
missing_brope = ((20 - bulgaria_rope_score) / 20 ) * 100

missing_iribbon = ((20 - italy_ribbon_score) / 20 ) * 100
missing_ihoop = ((20 - italy_hoop_score) / 20 ) * 100
missing_irope = ((20 - italy_rope_score) / 20 ) * 100

country = input()
discipline = input()

if country == "Russia":
    if discipline == "ribbon":
        print(f"The team of {country} get {russia_ribbon_score:.3f} on {discipline}.")
        print(f"{missing_rribbon:.2f}%")
    elif discipline == "hoop":
        print(f"The team of {country} get {russia_hoop_score:.3f} on {discipline}.")
        print(f"{missing_rhoop:.2f}%")
    elif discipline == "rope":
        print(f"The team of {country} get {russia_rope_score:.3f} on {discipline}.")
        print(f"{missing_rrope:.2f}%")

elif country == "Bulgaria":
    if discipline == "ribbon":
        print(f"The team of {country} get {bulgaria_ribbon_score:.3f} on {discipline}.")
        print(f"{missing_bribbon:.2f}%")
    elif discipline == "hoop":
        print(f"The team of {country} get {bulgaria_hoop_score:.3f} on {discipline}.")
        print(f"{missing_bhoop:.2f}%")
    elif discipline == "rope":
        print(f"The team of {country} get {bulgaria_rope_score:.3f} on {discipline}.")
        print(f"{missing_brope:.2f}%")

elif country == "Italy":
    if discipline == "ribbon":
        print(f"The team of {country} get {italy_ribbon_score:.3f} on {discipline}.")
        print(f"{missing_iribbon:.2f}%")
    elif discipline == "hoop":
        print(f"The team of {country} get {italy_hoop_score:.3f} on {discipline}.")
        print(f"{missing_ihoop:.2f}%")
    elif discipline == "rope":
        print(f"The team of {country} get {italy_rope_score:.3f} on {discipline}.")
        print(f"{missing_irope:.2f}%")

