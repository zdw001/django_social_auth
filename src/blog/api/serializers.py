from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    author = serializers.UserDetailSerializer(read_only=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)