# Mini AI Resume Analyzer

resume = input("Enter your resume skills: ").lower()

required_skills = [
    "python", "sql", "pandas",
    "numpy", "machine learning"
]

matched = []
missing = []

for skill in required_skills:
    if skill in resume:
        matched.append(skill)
    else:
        missing.append(skill)

score = len(matched) / len(required_skills) * 100

print("\n--- Resume Analysis ---")
print("Matched Skills:", matched)
print("Missing Skills:", missing)
print("Resume Match Score:", round(score, 2), "%")

if score >= 80:
    print("Excellent! Your skills match the job well.")
elif score >= 50:
    print("Good! Learn the missing skills.")
else:
    print("Keep learning and improving your skills.")