from models.ranking_model import top_scores


def get_rankings(level=None):
    return top_scores(level=level)
