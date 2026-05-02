from src.analysis.stance import country_issue_stance, dominant_stance
from src.analysis.alignment import country_alignment

country = "India"
country2 = "United States"

print("==== TESTING STANCE ====")
stance = country_issue_stance(country)
print(stance)

print("\n==== DOMINANT STANCE ====")
print(dominant_stance(stance))

print("\n==== ALIGNMENT TEST ====")
print(f"{country} vs {country2}:")
print(country_alignment(country, country2))