from django import template

register = template.Library()

@register.filter
def to_and(value):
    if "Listening Test" in value:
        return value.replace("Listening Test ","")
    elif "Reading Test" in value:
        return value.replace("Reading Test ", "")
    else:
        return value.replace("Writing Test ", "")
