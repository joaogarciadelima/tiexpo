from tiexpo.fabricantes import facade


def listar_fabricantes(request):
    return {'FABRICANTES': facade.listar_fabricantes_ordenados()}
