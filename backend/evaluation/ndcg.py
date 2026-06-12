import math


def ndcg(
    retrieved_ids,
    relevant_ids
):

    retrieved_unique = []

    seen = set()

    for video_id in retrieved_ids:

        if video_id not in seen:

            retrieved_unique.append(
                video_id
            )

            seen.add(video_id)

    dcg = 0

    for rank, video_id in enumerate(
        retrieved_unique,
        start=1
    ):

        if video_id in relevant_ids:

            dcg += (
                1 /
                math.log2(rank + 1)
            )

    ideal_dcg = 0

    num_relevant = len(
        relevant_ids
    )

    for rank in range(
        1,
        num_relevant + 1
    ):

        ideal_dcg += (
            1 /
            math.log2(rank + 1)
        )

    if ideal_dcg == 0:

        return 0

    return dcg / ideal_dcg