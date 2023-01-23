from django.urls import reverse

OTHER_USER = 'other_user'
TOTAL_POSTS = 13
LIMIT_POSTS_THREE = 3
LIMIT_POSTS_TEN = 10
USERNAME = 'User_test'
TEXT = 'text_test'
GROUP1_SLUG = 'slug_test'
GROUP1_TITLE = "Title"
GROUP1_DESCRIPTION = "descr_test"
GROUP2_TITLE = "Title2"
GROUP2_SLUG = "slug_test2"
GROUP2_DESCRIPTION = "descr_test2"
TWO_PAGE = 2
INDEX_HOME = '/'
INDEX = 'posts:index'
POST_CREATE = '/create/'
PROFILE = 'posts:profile'
POST_EDIT = 'posts:post_edit'
UNEXISTRING = '/unexisting_page/'
POST_DETAIL = 'posts:post_detail'
GROUP_LIST = 'posts:group_list'
INDEX_REV = reverse(INDEX)
PROFILE_REV = reverse(PROFILE, kwargs={'username': USERNAME})
POST_CREATE_REV = reverse('posts:post_create')
