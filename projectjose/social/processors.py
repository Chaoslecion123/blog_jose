from .models import Link,Direction

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx





    # direcions = Direction.objects.all()
    # for direction_ in direcions:
    #     return direction_
