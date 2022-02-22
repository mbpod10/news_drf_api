# NEWS django-rest-framework API

- Manual ArticleSerializer w/ Validations

```py
class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.location = validated_data.get('location', instance.location)
        instance.publication_date = validated_data.get(
            'publication_date', instance.publication_date)
        instance.active = validated_data.get('active', instance.active)
        instance.created_at = validated_data.get(
            'created_at', instance.created_at)
        instance.updated_at = validated_data.get(
            'updated_at', instance.updated_at)
        instance.save()
        return instance

    def validate(self, data):
        """Check if title and description are the same"""
        if data['title'] == data['description']:
            raise serializers.ValidationError(
                "Title and Description Must Be Different")
        return data

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "The title has to be at least 60 chars long")
        return value
```