import copy
from django.shortcuts import render
from django.http import JsonResponse
from Iterview_project.settings import RES_DATA
from RecordService.models import ClientScore
# Create your views here.


def index(request):
    """
    首页展示
    :return:
    """
    return render(request, 'index.html')


def save_record(request):
    """
    保存用户记录
    :param request:
    :return:
    """
    res_data = copy.deepcopy(RES_DATA)
    client_id = request.GET.get('client_id')
    score = request.GET.get('score')

    client_scores = ClientScore.objects.filter(client_name=client_id)

    if client_scores.exists():
        client_score = client_scores.first()
    else:
        client_score = ClientScore()

    if score or score == 0:
        client_score.client_name = client_id
        client_score.score = score
        client_score.save()
        print('ok')
    return JsonResponse(res_data)


def get_scores(request):
    """
    获取用户记录
    :param request:
    :return:
    """
    res_data = copy.deepcopy(RES_DATA)
    client_id = request.GET.get('client_id')
    from RecordService.util import select_query
    client_scores = select_query()
    client_id_score_lst = list()
    client_score_lst = list()
    for item in client_scores:
        if item.client_name == client_id:
            client_id_score_lst.append({'client_name': item.client_name, 'score': item.score})
        client_score_lst.append({'client_name': item.client_name, 'score': item.score})
    res_data['data'] = client_score_lst + client_id_score_lst
    return JsonResponse(res_data)


if __name__ == '__main__':
    save_record()
