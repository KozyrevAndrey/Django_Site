from django.contrib import admin

from .models import StatusCrm, Order, CommentCrm
# Register your models here.

class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ['comment_dt', 'comment_text']
    readonly_fields = ['comment_dt']
    extra = 0


class OrderAdm(admin.ModelAdmin):
    list_display = ['id', 'order_name', 'orders_phone', 'order_status', 'order_Dt']
    list_display_links = ['id', 'order_name']
    search_fields = ['order_name', 'order_status', 'order_phone']
    list_filter = ['order_status']
    list_editable = ['orders_phone', 'order_status']
    list_per_page = 20
    list_max_show_all = 50
    fields = ['id', 'order_Dt', 'order_status', 'order_name', 'orders_phone']
    readonly_fields = ('id', 'order_Dt')
    # Add class Comment for comment
    inlines = [
        Comment,
    ]




admin.site.register(StatusCrm)
admin.site.register(Order, OrderAdm)
admin.site.register(CommentCrm)
