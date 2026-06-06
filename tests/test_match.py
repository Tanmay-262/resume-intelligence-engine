from src.matcher import calculate_match_score

resume = """
Python
Machine Learning
SQL
NLP
"""

job_description = """
Python
Machine Learning
SQL
"""

score = calculate_match_score(
    resume,
    job_description
)

print(f"Match Score: {score}%")