from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def require_platform(allowed_user_agents, redirect_to = None):
    def decorator(func):
        def inner(request, *args, **kwargs):
            if 'HTTP_USER_AGENT' not in request.META:
                raise Http404()
            
            current_user_agent = request.META['HTTP_USER_AGENT']
            for user in allowed_user_agents:
                 if current_user_agent.find(user) != -1:
                    return func(request, *args, **kwargs)
            
            if redirect_to != None:
                return HttpResponseRedirect(reverse(redirect_to))
            else:
                raise Http404()
        return inner
    return decorator


require_iOS = require_platform(['iPhone', 'iPad'], redirect_to)