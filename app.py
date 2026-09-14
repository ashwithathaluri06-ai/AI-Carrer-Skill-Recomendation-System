from flask import Flask, render_template, request

app = Flask(__name__)

career_data = {
    "Data Analyst": {
        "skills": ["python", "sql", "excel", "power bi", "tableau", "statistics"],
        "interests": ["data", "analytics", "analysis", "business"],
        "learn": ["Advanced SQL", "Power BI", "Statistics", "Python Pandas"]
    },

    "Data Scientist": {
        "skills": ["python", "machine learning", "statistics", "pandas", "numpy"],
        "interests": ["data science", "data", "machine learning", "research"],
        "learn": ["Machine Learning", "Deep Learning", "Statistics", "Scikit-learn"]
    },

    "AI/ML Engineer": {
        "skills": ["python", "machine learning", "deep learning", "tensorflow", "pytorch"],
        "interests": ["ai", "artificial intelligence", "machine learning"],
        "learn": ["Deep Learning", "TensorFlow", "PyTorch", "NLP"]
    },

    "Software Developer": {
        "skills": ["java", "python", "c++", "programming", "git"],
        "interests": ["software", "programming", "development"],
        "learn": ["Data Structures", "Algorithms", "Git", "Software Development"]
    },

    "Web Developer": {
        "skills": ["html", "css", "javascript", "react", "web"],
        "interests": ["web", "website", "frontend", "backend"],
        "learn": ["JavaScript", "React", "Node.js", "Web Development"]
    },

    "UI/UX Designer": {
        "skills": ["figma", "design", "photoshop", "ui", "ux"],
        "interests": ["design", "ui", "ux", "creative"],
        "learn": ["Figma", "User Research", "Prototyping", "Design Systems"]
    },

    "Cybersecurity Analyst": {
        "skills": ["networking", "linux", "security", "cybersecurity", "python"],
        "interests": ["cybersecurity", "security", "ethical hacking", "cyber"],
        "learn": ["Network Security", "Linux", "Ethical Hacking", "Cybersecurity Tools"]
    },

    "Cloud Engineer": {
        "skills": ["aws", "azure", "cloud", "linux", "docker"],
        "interests": ["cloud", "cloud computing", "devops"],
        "learn": ["AWS/Azure", "Docker", "Linux", "DevOps"]
    },

    "Database Administrator": {
        "skills": ["sql", "mysql", "oracle", "database", "postgresql"],
        "interests": ["database", "data management", "sql"],
        "learn": ["Advanced SQL", "Database Security", "MySQL", "PostgreSQL"]
    }
}


@app.route("/", methods=["GET", "POST"])
def home():

    recommendation = None
    recommended_skills = []
    matched_skills = []
    match_percentage = 0
    match_level = ""
    name = ""
    reason = ""

    if request.method == "POST":

        name = request.form.get("name", "").strip().title()

        skills = request.form.get("skills", "").lower()

        user_skills = [
            skill.strip()
            for skill in skills.split(",")
            if skill.strip()
        ]

        interest = request.form.get("interest", "").lower()

        best_career = None
        highest_score = 0
        best_possible_score = 0

        for career, data in career_data.items():

            score = 0

            # Check skills
            for skill in data["skills"]:
                if skill in user_skills:
                    score += 2

            # Check interests
            for user_interest in data["interests"]:
                if user_interest in interest:
                    score += 3

            # Find the best matching career
            if score > highest_score:
                highest_score = score
                best_career = career

                best_possible_score = (
                    len(data["skills"]) * 2
                    + len(data["interests"]) * 3
                )

        # Display recommendation
        if best_career:

            recommendation = best_career

            recommended_skills = career_data[best_career]["learn"]

            # Find matching skills
            matched_skills = []

            for skill in career_data[best_career]["skills"]:

                if skill in user_skills:

                    if skill == "sql":
                        matched_skills.append("SQL")

                    elif skill == "aws":
                        matched_skills.append("AWS")

                    elif skill == "azure":
                        matched_skills.append("Azure")

                    elif skill == "ai":
                        matched_skills.append("AI")

                    elif skill == "ui":
                        matched_skills.append("UI")

                    elif skill == "ux":
                        matched_skills.append("UX")

                    else:
                        matched_skills.append(skill.title())

            reason = (
                "This career matches your current skills and interests. "
                "The recommended learning path will help you build stronger "
                "skills for this career."
            )

            # Calculate match percentage
            if best_possible_score > 0:

                match_percentage = round(
                    (highest_score / best_possible_score) * 100
                )

            # Determine match level
            if match_percentage >= 80:
                match_level = "Excellent Match"

            elif match_percentage >= 60:
                match_level = "Strong Match"

            elif match_percentage >= 40:
                match_level = "Good Match"

            else:
                match_level = "Developing Match"

        else:

            recommendation = "Software Developer"

            recommended_skills = career_data["Software Developer"]["learn"]

            match_percentage = 0

            match_level = "Developing Match"

    return render_template(
        "index.html",
        recommendation=recommendation,
        recommended_skills=recommended_skills,
        match_percentage=match_percentage,
        match_level=match_level,
        name=name,
        reason=reason,
        matched_skills=matched_skills
    )


if __name__ == "__main__":
    app.run(debug=True)

