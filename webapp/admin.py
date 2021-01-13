from django.contrib import admin
from .models import employees
from .models import reservation
from .models import CHAMBREDEP
from .models import CHAMBREARR
from .models import CHAMBREHORS

admin.site.register(employees)
admin.site.register(reservation)
admin.site.register(CHAMBREDEP)
admin.site.register(CHAMBREARR)
admin.site.register(CHAMBREHORS)



# Register your models here.
