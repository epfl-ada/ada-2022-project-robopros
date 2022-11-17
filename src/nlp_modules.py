from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
from fast_pagerank import pagerank
import numpy as np

def gen_match_matrix(model, sents, min_match_score=0):
    """Generate a matrix of sentence matches for a list of sentences"""
    sents1 = [x for x in sents]
    sents1_embeddings = model.encode(sents1)
    sim_matrix = cosine_similarity(sents1_embeddings, sents1_embeddings)
    super_threshold_indices = sim_matrix < min_match_score
    sim_matrix[super_threshold_indices] = 0
    # print(sim_matrix)
    return sim_matrix


def filter_ranked_list(ranked_sents, model, min_match=0.8, N=3):
    """a ranked list of sentences is filtered by removing sentences that are too similar to other sentences in the list
    N is the number of sentences to return"""
    ranked_sents = [x[0] for x in ranked_sents]
    filtered_sents = []
    for i, s in enumerate(ranked_sents):
        if len(filtered_sents) >= N or len(filtered_sents) >= len(ranked_sents):
            break
        if len(filtered_sents) == 0:
            filtered_sents.append(s)
        else:
            matching_scores = gen_match_matrix(model, [s] + filtered_sents)
            max_sim = np.max(matching_scores[0][1:])
            # print(matching_scores)
            if max_sim < min_match:
                filtered_sents.append(s)

        # print(min_match)

    return filtered_sents


def apply_page_rank(sentences, p=0.85, min_match_score=0.5, min_len=5, max_len=35):
    """Apply page rank to a list of sentences
    min_match_score: minimum similarity score for two sentences to be considered similar
    min_len: minimum length of a sentence
    max_len: maximum length of a sentence
    returns a ranked list of sentences
    """
    cand_sents = [x for x in sentences if len(
        x.split()) < max_len and len(x.split()) > min_len]
    if len(cand_sents) == 0:
        # print('empty')
        return []
    # print(cands)
    # print(cands_qualities)
    cands_matching_mat = gen_match_matrix(
        model, cand_sents, min_match_score=min_match_score)
    # it looks like modifying the initial probability doesn't help
    pr = pagerank(cands_matching_mat, p=p)
    # pr=pagerank(cands_matching_mat, p=p)
    ranked_candidates = list(zip(cand_sents, pr))
    return sorted(ranked_candidates, key=lambda x: -x[1])
