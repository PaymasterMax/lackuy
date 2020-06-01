from django import template

register = template.Library()
@register.filter("check_user")
def identify_user(chat_user_id , current_user_id):
    if chat_user_id==current_user_id:
        return True

    else:
        return False
