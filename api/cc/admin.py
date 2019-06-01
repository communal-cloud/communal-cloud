from django.contrib import admin

from .models import *

class BaseModelAdmin(admin.ModelAdmin):
	readonly_fields = ('CreatedOn', 'ModifiedOn')

admin.site.register(BaseModel)
admin.site.register(Role)
admin.site.register(Category)
admin.site.register(DataEnumeration)
admin.site.register(DataField)
admin.site.register(DataType)
admin.site.register(Task)
admin.site.register(ExecutionData)
admin.site.register(Execution)
admin.site.register(Workflow)
admin.site.register(Community)
admin.site.register(Member)
admin.site.register(User)


