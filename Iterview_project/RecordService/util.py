
from RecordService.models import ClientScore


def select_query(condition=None):
    """
    查询函数
    :return:
    """
    if condition:
        client_scores = ClientScore.objects.filter(client_name=condition)
    else:
        client_scores = ClientScore.objects.filter().all().order_by('score')
    return client_scores


