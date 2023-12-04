from rest_framework import serializers
from book_app.models import Book, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('book',)
        #fields = "__all__"


class BookListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    # platform = serializers.CharField(source='platform.name')
    
    #avg_rating = serializers.ReadOnlyField
    #number_rating = serializers.ReadOnlyField

    class Meta:
        model = Book
        fields = "__all__"


# class StreamPlatformSerializer(serializers.ModelSerializer):
#     watchlist = WatchListSerializer(many=True, read_only=True)

#     class Meta:
#         model = StreamPlatform
#         fields = "__all__"