from django.contrib.comments.models import Comment

# To fix TextField problem of django's comment framework
# See 
FIELD_INDEXES = {
    Comment: {'indexed': ['object_pk', 'comment']},
}