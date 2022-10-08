from typing import List

class CountVectorizer:
    '''CountVectorizer class implementation'''
    def __init__(self, lowercase=True):

        self.lowercase = lowercase
        self.unique_words = None

    def fit_transform(self, corpus: List[str]) -> List[List[str]]:
        '''Function returns count matrix'''

        if self.lowercase:
            corpus = [doc.lower() for doc in corpus]

        # create a set of unique words - we will also use them in get_feature_names() method

        unique_words = set()
        for doc in corpus:
            unique_words.update(doc.split())

        unique_words = list(unique_words)
        unique_words.sort()  # for reproducibility
        self.unique_words = unique_words

        count_matrix = []

        for doc in corpus:

            doc_dict = {word: 0 for word in self.unique_words}
            for word in doc.split():
                if word in doc_dict:
                    doc_dict[word] += 1
                else:
                    doc_dict[word] = 1

            count_matrix.append(list(doc_dict.values()))

        return count_matrix

    def get_feature_names(self):
        '''Function returns list of unique words'''
        if not self.unique_words:
            raise ValueError('Fit the vectorizer first')
        return self.unique_words
        
