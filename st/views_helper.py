import inspect

def funct_name_html():
    '''returns the name of the caller function and adds ".html" '''
    name = inspect.stack()[1][3]
    return  name + '.html'

def prepare_context(query):

    attrs = vars(query)
    attrs.pop('_state')
    context = attrs.items()
    return context

def prepare_list_context(query):

    context = []
    for i in query:
        attrs = vars(i)
        attrs.pop('_state')
        context.append(attrs.items())
    return context