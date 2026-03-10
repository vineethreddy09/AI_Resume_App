def match_skills(resume_text, skills):

    matched = []
    missing = []

    if len(skills) == 0:
        return 0, matched, missing

    for skill in skills:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (len(matched) / len(skills)) * 100

    return score, matched, missing