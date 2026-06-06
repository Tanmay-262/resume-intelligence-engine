from matcher import calculate_match_score


def rank_candidates(candidates, job_description):

    results = []

    for candidate in candidates:

        score = calculate_match_score(
            candidate["resume_text"],
            job_description
        )

        results.append({
            "name": candidate["name"],
            "score": score
        })

    ranked = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked