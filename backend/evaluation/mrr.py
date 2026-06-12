def reciprocal_rank(retrieved_ids,relevant_ids):

    relevant_ids = set(relevant_ids)

    for rank,id in enumerate(retrieved_ids,start=1):

        if id in relevant_ids:
            return 1/rank

    return 0
        