def nutrition_score(nutrition, state):
    if not nutrition:
        return 0

    calories = nutrition[0]
    protein = nutrition[4]

    if state["nutrition"] == "protein":
        return protein * 0.5

    return -calories * 0.001


def tag_score(tags, state):
    score = 0

    if state["effort"] == "low" and "15-minutes-or-less" in tags:
        score += 0.3

    if state["emotion"] == "comfort" and "soups-stews" in tags:
        score += 0.3

    return score


def final_score(row, sim, state):
    score = sim

    score += nutrition_score(row["nutrition"], state)
    score += tag_score(row["tags"], state)

    return score

