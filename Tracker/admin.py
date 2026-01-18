from django.contrib import admin
from Tracker.models import *    


admin.site.site_header = "Budget Tracker"
admin.site.site_title = "Budget Tracker"    


admin.site.register(CurrentBalance)


class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = ('description', 'amount', 'expense_type', 'created_at')
    list_filter = ('expense_type',)
    search_fields = ('description',)
    ordering = ('-created_at',)

    
admin.site.register(TrackingHistory, TrackingHistoryAdmin)