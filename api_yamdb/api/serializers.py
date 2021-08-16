from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from reviews.models import Category, Comment, Genre, Review, Title

from django.db.models import Avg


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Category


class CategoryField(serializers.SlugRelatedField):

    def to_representation(self, value):
        return CategorySerializer(value).data


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('id',)
        model = Genre


class GenreField(serializers.SlugRelatedField):

    def to_representation(self, value):
        return GenreSerializer(value).data


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all()
    )
    category = CategoryField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    rating = serializers.IntegerField(
        read_only=True,
        required=False,
        min_value=1,
        max_value=10
    )

    class Meta:
        fields = '__all__'
        model = Title

    # def get_rating(self, obj):
    #     if Title.objects.all().annotate(rating=Avg('reviews__score')).get('reviews__score__avg') is None:
    #         return 0
    #     return Title.objects.all().annotate(rating=Avg('reviews__score')).get('reviews__score__avg')


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.PrimaryKeyRelatedField(read_only=True)
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.PrimaryKeyRelatedField(read_only=True)
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
