from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
import requests

from csd.models import Counterpart, Entry


@view_config(route_name='comment', request_method='POST')
def comment(request):  # pragma: no cover
    """check whether a blog post for the datapoint does exist.

    if not, create one and redirect there.
    """
    cls = Entry if request.matchdict['type'] == 'Entry' else Counterpart
    obj = cls.get(request.matchdict['id'])
    return HTTPFound(request.blog.post_url(obj, request, create=True))


@view_config(route_name='comments')
def comments(request):
    request.blog.feed_url('comments/feed/', request)
    res = requests.get(request.blog.feed_url('comments/feed/atom/', request))
    return Response(res.text, content_type="application/xml")
