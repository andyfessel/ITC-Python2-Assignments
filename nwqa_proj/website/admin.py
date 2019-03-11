from django.contrib import admin
from .models import Blog
from .models import HomeOwner
from .models import Project
from .models import Traffic
from .models import Safety
from .models import NeedGoodNeighbor
from .models import BeGoodNeighbor
from .models import Emergency
from .models import Celebrations

admin.site.register(Blog)
admin.site.register(HomeOwner)
admin.site.register(Project)
admin.site.register(Traffic)
admin.site.register(Safety)
admin.site.register(NeedGoodNeighbor)
admin.site.register(BeGoodNeighbor)
admin.site.register(Emergency)
admin.site.register(Celebrations)

