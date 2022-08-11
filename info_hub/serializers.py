from rest_framework import serializers


from .models import *

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id','content', 'post', 'user', 'date_created']

    def save(self, **kwargs):
        user = self.context['user']

        self.instane = Post.objects.create(user = user , **self.validated_data)

        return self.instance

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['content', 'attachment', 'user', 'date_created', 'comments','comment_count']

    def get_comment_count(self, obj):
        return obj.comments.count()

    def save(self, **kwargs):
        user = self.context['user']

        if user.NIN:
            raise ValidationError("You are not allowed to make post")
        
        else:
            self.instane = Post.objects.create(user = user , **self.validated_data)

        return self.instance


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'date']


class NewsletterSerializer(serializers.ModelSerializer):
    #email = serializers.EmailField()

    class Meta:
        model = Newsletter
        fields = ['id','email']
