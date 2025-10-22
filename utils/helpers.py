import numpy as np

def _compute_delta_ent(i, j, weights):
    """
    Entropy change on merging two clusters (following Baudry).
    """
    delta_ent = 0.0
    for w in weights:  # each w is a vector of weights (this is a loop over particles)
        w_merge = w[i] + w[j]  # for this particle, add the weights for cluster i and j
        delta_ent += w_merge * np.log(w_merge)
        if w[i] > 0.0:
            delta_ent -= w[i] * np.log(w[i])
        if w[j] > 0.0:
            delta_ent -= w[j] * np.log(w[j])
    return delta_ent


def _compute_ICL_ent(weights, epsilon_):
    """
    ICL entropy from list of weights.
    """
    ICL_ent = 0.0
    for w in weights:
        wts = np.maximum(w, epsilon_)
        ICL_ent -= np.sum(wts * np.log(wts))
    return ICL_ent



def merge_clusters(weights, n_clusters_min=2, epsilon_=1e-15):
    """
    Merge clusters into ``n_clusters_min`` new clusters based on the
    probabilities that particles initially belong to each of the original
    clusters with a certain probability and using an entropy criterion.
    
    See https://doi.org/10.1198/jcgs.2010.08111 (Baudry et al.).

    Parameters
    ----------
    weights : list
        Probabilities that each particle belongs to each cluster.
        If there are :math`N` particles, then the length of the list (or first
        dimension of the array) must be :math:`N`. If there are math:`K` original
        clusters, each element of ``weights`` (or the first dimension of the array)
        must be :math:`K`. ``weights[i][j]`` (list) or ``weights[i,k]`` (array) is the 
        probability that particle ``i`` belongs to cluster ``k`` before merging.
        For each particle, ``sum(weights[i])`` is equal to 1.

    n_clusters_min : int, default: 2
        Final number of clusters after merging.

    epsilon_ : float
        Small number (close to zero). This is needed as a replacement for zero
        when computing a logarithm to avoid errors.

    Returns
    -------
    new_weights : np.ndarray
        New weights after merging. Same shape and interpretation as the
        ``weights`` input parameter.

    new_labels : list
        New discrete labels based on the weights after merging.
    """
    new_weights = np.asarray(weights).copy()

    # number of clusters (to be changed during the merge)
    n_clusters = weights[0].size

    # print("# i  j  delta_entropy")
    while n_clusters > n_clusters_min:
        # loop over all pairs of clusters and consider what happens if we merge
        d_evals = []
        labs = []
        for i in range(new_weights[0].size):  # i loops over clusters
            for j in range(i):
                delta_ent = _compute_delta_ent(i, j, new_weights)
                d_evals.append(delta_ent)
                labs.append([i, j])

        best_merge_index = d_evals.index(max(d_evals))

        for w in new_weights:
            w[labs[best_merge_index][1]] += w[labs[best_merge_index][0]]
            w[labs[best_merge_index][0]] = epsilon_

        n_clusters -= 1

    # new discrete labels based on the new weights
    new_labels = [0 for n in range(new_weights.shape[0])]
    for i, wi in enumerate(new_weights):
        new_labels[i] = np.argmax(wi)

    return new_weights, new_labels