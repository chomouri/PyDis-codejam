from django.conf import settings
from django.db import models
from django.utils.crypto import get_random_string


def generate_id():
    return get_random_string(20)


class ChessMatch(models.Model):
    CHESS_MATCH_TYPES = [
        ("confusion_chess", "Confusion chess"),
        ("magic_chess", "Magic chess")
    ]
    id = models.SlugField(allow_unicode=True, primary_key=True, default=generate_id)
    white = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                              related_name="chess_match_white")
    black = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                              related_name="chess_match_black")
    type = models.CharField(max_length=50, choices=CHESS_MATCH_TYPES)
    starting_pos = models.TextField(default="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    created_at = models.DateTimeField(auto_now_add=True)
    result = models.IntegerField(choices=((0, "Draw"), (1, "White wins"), (-1, "Black wins")), null=True, blank=True)
