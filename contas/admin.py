from django.contrib import admin
from .models import Categoria
from .models import Transacao
from .models import Trabalhos
from .models import Caracteristica

admin.site.register(Categoria)
admin.site.register(Transacao)
admin.site.register(Trabalhos)
admin.site.register(Caracteristica)
