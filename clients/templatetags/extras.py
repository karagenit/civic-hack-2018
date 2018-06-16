from django import template

register = template.Library()

@register.filter(name='get_count_including_cart')
def get_count_including_cart(item, user):
    available = item.get_count()
    cart = user.profile.client.get_num_items_in_cart(item)
    return (available - cart)
    
