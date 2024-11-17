from django.forms import ModelForm
from django.views.generic import CreateView
from django.urls import reverse
from shortener_app.models import AliasedUrl  # Ensure this import is here


class AliasedUrlForm(ModelForm):
    class Meta:
        model = AliasedUrl
        fields = ['url']

class AliasCreateView(CreateView):
    form_class = AliasedUrlForm
    template_name = 'create_alias.html'

    def get_success_url(self):
        return f"{reverse('create')}?created_alias={self.object.alias}"
