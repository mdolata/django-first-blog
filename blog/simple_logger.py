import os
from django.utils import timezone


# simple logger
# TODO: change my simple logger to something better and recommended
def logger(request, method):
    path = os.path.join('logs', method + '.txt')
    f = open(path, 'a')
    f.write(str(request)
            + '   -~>    ' + str(timezone.now())
            + ' ip: ' + get_client_ip(request)
            + ' ' + get_user_name(request)
            + '\n')
    f.close()


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_user_name(request):
    return request.user.username
