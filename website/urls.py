from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('automatosFinitos/', views.automatosFinitos, name='automatosFinitos'),
    path('novoAutomato/', views.novoAutomato, name='novoAutomato'),
    path('<int:automato_id>/validarAutomato/', views.validarAutomato, name='validarAutomato'),
    path('editarAutomato/<int:automato_id>/', views.editarAutomato, name='editarAutomato'),
    path('apagarAutomato/<int:automato_id>/', views.apagarAutomato, name='apagarAutomato'),
    path('expressoesRegulares/', views.expressoesRegulares, name='expressoesRegulares'),
    path('novoExpressao/', views.novoExpressao, name='novoExpressao'),
    path('<int:expressao_id>/validarExpressao/', views.validarExpressao, name='validarExpressao'),
    path('editarExpressao/<int:expressao_id>/', views.editarExpressao, name='editarExpressao'),
    path('apagarExpressao/<int:expressao_id>/', views.apagarExpressao, name='apagarExpressao'),
    path('maquinasTuring/', views.maquinasTuring, name='maquinasTuring'),
    path('novoMaquina/', views.novoMaquina, name='novoMaquina'),
    path('<int:maquina_id>/validarMaquina/', views.validarMaquina, name='validarMaquina'),
    path('editarMaquina/<int:maquina_id>/', views.editarMaquina, name='editarMaquina'),
    path('apagarMaquina/<int:maquina_id>/', views.apagarMaquina, name='apagarMaquina')   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)