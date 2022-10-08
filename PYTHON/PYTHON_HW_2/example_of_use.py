from count_vectorizer import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer as SklearnCountVectorizer

corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]

vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)


if __name__ == '__main__':

    print("Count matrix:")
    print(count_matrix)

    print("Feature names:")
    print(vectorizer.get_feature_names())

    # Let's compare the results with sklearn's CountVectorizer for fun

    skl_count_vectorizer = SklearnCountVectorizer()
    skl_count_matrix = skl_count_vectorizer.fit_transform(corpus)

    print("Sklearn count matrix:")
    print(skl_count_matrix.toarray())

    print("Sklearn feature names:")
    print(skl_count_vectorizer.get_feature_names())

'''
Output:
Count matrix:
[[1, 1, 1, 0, 0, 1, 0, 2, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]]
Feature names:
['again', 'boil', 'crock', 'fresh', 'ingredients', 'never', 'parmesan', 'pasta', 'pomodoro', 'pot', 'taste', 'to']
Sklearn count matrix:
[[1 1 1 0 0 1 0 2 0 1 0 0]
 [0 0 0 1 1 0 1 1 1 0 1 1]]
Sklearn feature names:
['again', 'boil', 'crock', 'fresh', 'ingredients', 'never', 'parmesan', 'pasta', 'pomodoro', 'pot', 'taste', 'to']
'''