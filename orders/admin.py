from django.core.urlresolvers import reverse
from django.contrib import admin
from .models import Order, OrderItem
from django.http import HttpResponse
import csv
import datetime


# Register your models here.

# adding a view button to the admin
def order_detail(obj):
    return '<a href="{}">View</a>'.format(reverse('orders:admin_order_detail', args=[obj.id]))


order_detail.allow_tags = True
"""
Set the allow_tags attribute to True to avoid HTML-escaping in any Model method,
 ModelAdmin method, or any other callable. When you
use allow_tags, make sure to escape input that has come from the user to avoid cross-site scripting.
"""


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


# export order ho a csv file
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # write the first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created_date', 'updated_date', order_detail]
    list_filter = ['paid', 'created_date', 'updated_date', ]
    inlines = [OrderItemInLine]

    actions = [export_to_csv]


admin.site.register(Order, OrderAdmin)
