from django import template

register = template.Library()

#custom template filters below

@register.filter(name='cut') #using decorator to register the filter
def cut(value,arg):
    #cuts out arg from string
    return value.replace(arg, '')

#register the custom template filter (or use decorator as seen above)
#register.filter('cut',cut)
