from rest_framework import serializers


from .models import *

class AddCommentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

    def save(self, **kwargs):
        user = self.context['user']
        post_id = self.context['post_id']

    
        self.instance = Comment.objects.create(user = user , post_id = post_id , **self.validated_data)
 
        return self.instance

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id','content','user', 'date_created']

    

class AddPostSerializer (serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = ['content', 'attachment']

    def save(self, **kwargs):
        user = self.context['user']

        if user.NIN:
            raise ValidationError("You are not allowed to make post")
        
        else:
            self.instance = Post.objects.create(user = user , **self.validated_data)

        return self.instance


class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id','content', 'attachment', 'user', 'date_created','comment_count']

    def get_comment_count(self, obj):
        return obj.comments.count()




class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'date']


class NewsletterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Newsletter
        fields = ['id','email']
