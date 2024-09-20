import math

def compute_idf(corpus):
    """
    Computes the Inverse Document Frequency (IDF) for each term in the corpus.
    
    Parameters:
    corpus (list of list of str): A list of documents, where each document is represented as a list of terms (words).
    
    Returns:
    dict: A dictionary with terms as keys and their IDF scores as values.
    """
    idf_dict = {}
    N = len(corpus)  # Total number of documents in the corpus
    
    # Calculate document frequency for each term
    for document in corpus:
        for term in set(document):
            if term in idf_dict:
                idf_dict[term] += 1
            else:
                idf_dict[term] = 1
    
    # Compute IDF for each term
    for term, count in idf_dict.items():
        idf_dict[term] = math.log(N / float(count)) + 1  # Adding 1 to prevent division by zero
    
    return idf_dict

# Example usage
corpus = [
    ["the", "quick", "brown", "fox"],
    ["jumped", "over", "the", "lazy", "dog"],
    ["the", "dog", "barked", "at", "the", "fox"]
]

idf_scores = compute_idf(corpus)
print("IDF Scores:", idf_scores)
