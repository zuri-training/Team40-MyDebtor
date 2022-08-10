from rest_framework import serializers


from .models import *

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id','content', 'post', 'user', 'date_created']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        return obj.comments.count()

    class Meta:
        model = Post
        fields = ['content', 'attachment', 'user', 'date_created', 'comments','comment_count']

    def create(self, validated_data):
        comments_data = validated_data.pop('comments')
        post = Post.objects.create(**validated_data)
        Comment.objects.create(post=post, **comments_data)
        return post



class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'date']


class NewsletterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Newsletter
        fields = ['email']
