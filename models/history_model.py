from models.result_model import get_results_by_user


def user_history(user_id):
    return get_results_by_user(user_id)
