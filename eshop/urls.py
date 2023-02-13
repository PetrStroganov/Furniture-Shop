from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("furniture.urls")),
    path('accounts', include("accounts.urls"))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 1) Создать приложение accounts, и сделать в нем правильную структуру проекта (не забыть про urls и прочее)
# 2) Создать самостоятельно новый проект, тематику проект выбрать любую, но сделать его до текущего состояние нашего проекта
