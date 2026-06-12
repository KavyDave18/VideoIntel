def recall_at_k(retrieved_ids,relevant_ids):

    retrieved_ids = set(retrieved_ids)

    relevant_ids = set(relevant_ids)

    relevant_retrived = len(retrieved_ids.intersection(relevant_ids))

    return relevant_retrived/len(relevant_ids)

def precision_at_k(retrieved_ids,relevant_ids):


    relevant_ids = set(relevant_ids)

    relevant_retrived = 0

    for id in retrieved_ids:
        if id in relevant_ids:
            relevant_retrived+=1

    return relevant_retrived/len(retrieved_ids)