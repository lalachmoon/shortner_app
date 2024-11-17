from django.shortcuts import redirect, get_object_or_404
from shortener_app.models import AliasedUrl

def redirect_view(request, alias):
    aliased_url = get_object_or_404(AliasedUrl, alias=alias)
    return redirect(aliased_url.url)
