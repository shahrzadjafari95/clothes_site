from django import template

register = template.Library()


@register.filter
def format_price(value):
    # Check if the price is a whole number
    if value.is_integer():
        return int(value)  # Remove the decimal point and return as an integer
