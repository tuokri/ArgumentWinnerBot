from praw.models.comment_forest import CommentForest


def evaluate_comment_reply_pair(comment) -> CommentForest:
    reply = next(comment.replies)

    return reply
