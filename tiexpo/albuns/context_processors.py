from tiexpo.albuns import facade


def listar_albuns(request):
    return {'ALBUNS': facade.listar_albuns_ordenados()}
