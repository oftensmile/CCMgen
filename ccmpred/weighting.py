import numpy as np


def weights_uniform(msa):
    """Uniform weights"""
    return np.ones((msa.shape[0],), dtype="float64")


def weights_simple(msa, cutoff=0.8):
    """Simple sequence reweighting from the Morcos et al. 2011 DCA paper"""

    if cutoff >= 1:
        return weights_uniform(msa)

    ncol = msa.shape[1]

    # calculate pairwise sequence identity between all alignments
    ids = np.sum(msa[:, np.newaxis, :] == msa[np.newaxis, :, :], axis=2)

    # calculate number of cluster members at identity cutoff
    n_cluster = np.sum(ids > cutoff * ncol, axis=0)

    return (1 / n_cluster.astype("float64"))
