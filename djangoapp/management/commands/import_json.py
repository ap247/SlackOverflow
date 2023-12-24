import json
from django.core.management.base import BaseCommand
from djangoapp.models import Comment
from djangoapp.serializers import CommentSerializer
from django.db import connection

class Command(BaseCommand):
    help = 'Load a list of items from a JSON file into the database'

    def handle(self, *args, **kwargs):
        with open('djangoapp/static/comments.json', 'r') as file:
            data = json.load(file)
            comments_data = data['comments']
            max_id = 0
            for item in comments_data:
                if not Comment.objects.filter(id = item['id']).exists():
                    Comment.objects.create(**item)
                else:
                    comment = Comment.objects.get(id=item['id'])
                    serializer = CommentSerializer(instance=comment, data=item)
                    
                    if serializer.is_valid():
                        serializer.save()
                max_id = max(max_id, int(item['id']))
            
            # Reset primary key sequence
            with connection.cursor() as cursor:
                cursor.execute("SELECT setval('djangoapp_comment_id_seq', %s, false)", [max_id + 1])