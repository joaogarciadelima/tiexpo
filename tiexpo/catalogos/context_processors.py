from tiexpo.catalogos import facade


def listar_catalogos(request):
    return {'CATALOGOS': facade.listar_catalogos_ordenados()}


def listar_fabricantes(request):
    return {'FABRICANTES': facade.listar_fabricantes_ordenados()}
