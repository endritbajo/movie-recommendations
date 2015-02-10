__author__ = 'endrit bajo'

import distances import utils

class Dataset:
    data = {}
    similar_items = {}

    def __init__(self, data):
        self.data = data

    def get():
        return data

    def flip():
        """
        Transform dataset. Transform the data from:
        data = {
            item1 : {
                subitem1: value_11,
                subitem2: value_12,
                ...
                subitemn: value_1n
            }
            ...
            itemn : {
                subitem1: value_n1,
                subitem2: value_n2,
                ...
                subitemn: value_nn
            }
        }

        to:
        data = {
            subitem1 : {
                item1: value_11,
                item2: value_12,
                ...
                itemn: value_1n
            }
            ...
            subitemn : {
                item1: value_n1,
                item2: value_n2,
                ...
                itemn: value_nn
            }
        }
        """
        result = {}
        for item in data:
            for subitem in data[item]:
                result.setdefault(subitem, {})
                # flip item and subitem
                result[subitem][item] = data[item][subitem]

        return result

    def build_similar_items_dataset(data, n = 5):
        """
        Computes the dataset of similar items (item-based filtering).
        Needs to be run once in a while to keep the similarity updated.
        The fewer the data at disposal more frequent you need to run this method.
        """
        transformed_data = transform_dataset(data)

        items = {}

        for item in transformed_data:
            items[item] = similar_items(transformed_data, item, similarity = distances.pearson_correlation, n = n)

        return items

    def similar_items(data, myitem, similarity = distances.pearson_correlation, n = 5):
        """
        Given an item, it returns items similar to each other (similar movies or similar users).
        If you want similar users, the data is a dictionary structured in the following way:

        data = {
            user1 : {
                movie1: rating1,
                movie2: rating2,
                ...
                movien: ratingn
            }
            ...
            usern : {
                movie1: rating1,
                movie2: rating2,
                ...
                movien: ratingn
            }
        }

        If you want similar movies:

        data = {
            movie1 : {
                user1: rating1,
                user2: rating2,
                ...
                usern: ratingn
            }
            ...
            movien : {
                user1: rating1,
                user2: rating2,
                ...
                usern: ratingn
            }
        }
        """
        items = [(similarity(data, myitem, other), other) for other in data if other != myitem]
        items.sort()
        items.reverse()

        return items[0:n]

    def recommended_movies(data, person, similarity = distances.pearson_correlation, n = 5):
        """
        Given a user, it returns a list of recommended movies (user-based filtering).
        The data is a dictionary structured in the following way:

        data = {
            user1 : {
                movie1: rating1,
                movie2: rating2,
                ...
                movien: ratingn
            }
            ...
            usern : {
                movie1: rating1,
                movie2: rating2,
                ...
                movien: ratingn
            }
        }
        """
        # total movie score
        total_score = {}
        # total movie similarities
        total_similarities = {}

        for user in data:
            if user == person:
                continue

            sim = similarity(data, person, user)

            # ignore score of zero or lower
            if sim <= 0:
                continue

            for (movie, rating) in data[user].items():
                # if user has not yet seen the movie
                if movie not in data[person] or rating == 0:
                    # similarity * score
                    total_score.setdefault(movie, 0)
                    total_score[movie] += rating * sim
                    # sum of similarities
                    total_similarities.setdefault(movie, 0)
                    total_similarities[movie] += sim

        movies = [(total / total_similarities[movie], movie) for (movie, total) in total_score.items()]

        movies.sort()
        movies.reverse()

        return movies[0:n]
