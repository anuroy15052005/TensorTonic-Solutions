def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    top_k = recommended[0:k]
    hit = 0
    for x in top_k:
        if x in relevant:
            hit += 1

    precision = hit/k
    recall = hit/len(relevant)
    return [precision, recall]
    # Write code here
    pass