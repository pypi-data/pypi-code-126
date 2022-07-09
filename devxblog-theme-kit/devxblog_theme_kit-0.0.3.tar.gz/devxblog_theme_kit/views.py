from django.utils import timezone
from django.views.generic import TemplateView


class ThemePageView(TemplateView):
    template_name = 'page_view.html'

    def get_context_data(self, **kwargs):
        context = super(ThemePageView, self).get_context_data(**kwargs)
        context['theme'] = {
            'name': 'My theme',
        }
        context['page'] = {
            'title': 'Example Page Name',
            'slug': 'page-slug',
            'date_created': timezone.datetime(2022, 6, 1, 12, 0, 0),
            'date_updated': timezone.datetime(2022, 6, 2, 13, 30, 22),
            'content': """
                <h1>This is the page title</h1>

                <h2>This is a subtitle</h2>

                <p>This is a paragraph</p>
            """,
            'protected': False
        }
        context['blog'] = {
            'id': 'blog-id',
            'domain': 'example.com',
            'free_subdomain': 'example.devxblog.com',
            'favicon': '/static/favicon.png',
            'logo': '/static/logo.png',
            'date_created': timezone.datetime(2022, 5, 1),
            'date_updated': timezone.datetime(2022, 5, 2),
            'theme': context['theme'],
            'theme_variables': {

            },
            'navigation': [
                {
                    'kind': 'External',
                    'href': 'http://google.com',
                    'display': 'My twitter account'
                },
                {
                    'kind': 'Link',
                    'target': '/page/hobbies/',
                    'display': 'Hobbies'
                },
                {
                    'kind': 'Dropdown',
                    'display': 'Blog',
                    'items': [
                        {
                            'kind': 'Link',
                            'target': '/posts/?category=tech',
                            'display': 'Technology'
                        },
                        {
                            'kind': 'Link',
                            'target': '/posts/?category=tips',
                            'display': 'Tips and tricks'
                        },
                        {
                            'kind': 'Link',
                            'target': '/posts/?category=thoughts',
                            'display': 'Thoughts'
                        },
                        {
                            'kind': 'Separator'
                        },
                        {
                            'kind': 'Blog',
                            'display': 'All posts'
                        },
                        {
                            'kind': 'External',
                            'href': 'http://facebook.com',
                            'display': 'test'
                        }
                    ]
                },
                {
                    'kind': 'Link',
                    'target': '/page/projects/',
                    'display': 'Projects'
                },
                {
                    'kind': 'Dropdown',
                    'display': 'Social Links',
                    'items': [
                        {
                            'kind': 'External',
                            'display': 'Twitter',
                            'href': 'https://twitter.com/stefanvladcalin'
                        },
                        {
                            'kind': 'External',
                            'display': 'Facebook',
                            'href': 'https://www.facebook.com/vlad.calin1'
                        },
                        {
                            'kind': 'External',
                            'display': 'Linkedin',
                            'href': 'https://www.linkedin.com/in/calinstefanvlad'
                        },
                        {
                            'kind': 'External',
                            'display': 'Gitlab',
                            'href': 'https://gitlab.com/vladcalin'
                        }
                    ]
                }
            ],
            'social': {
                'twitter': '',
                'linkedin': '',
                'facebook': '',
                'github': '',
                'gitlab': '',
            },
        }
        return context


class ThemePostView(TemplateView):
    template_name = 'post_view.html'


class ThemePostList(TemplateView):
    template_name = 'post_list.html'
