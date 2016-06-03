from django.conf.urls import url, include
from myblog.views import stub_view, list_view, detail_view
from myblog.views import PostCreate, PostUpdate


urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    url(r'^posts/(?P<post_id>\d+)/$',
        detail_view,
        name='blog_detail'),
    url(r'post/add/$', 
    	PostCreate.as_view(), 
    	name='post-add'),
    url(r'post/(?P<pk>[0-9]+)/$', 
    	PostUpdate.as_view(), 
    	name='post-update'),
]