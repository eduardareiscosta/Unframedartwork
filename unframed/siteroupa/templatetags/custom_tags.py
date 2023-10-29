from django import template
from ..models import Order

register = template.Library()

@register.simple_tag
def order_quantity(user):
    return Order.objects.filter(user=user).aggregate(total_quantity=models.Sum(quantity))