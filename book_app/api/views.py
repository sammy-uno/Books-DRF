from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, ScopedRateThrottle, UserRateThrottle
from rest_framework.views import APIView

from book_app.api  import pagination, permissions, serializers, throttling
from book_app.models import Review, Book


class UserReview(generics.ListAPIView):
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        return Review.objects.filter(review_user__username=username)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = serializers.ReviewSerializer
    permission_classes = [IsAuthenticated]
    #throttle_classes = [throttling.ReviewCreateThrottle]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(book=book, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")

        if book.number_rating == 0:
            book.avg_rating = serializer.validated_data['rating']
        else:
            book.avg_rating = (book.avg_rating + serializer.validated_data['rating'])/2

        book.number_rating = book.number_rating + 1
        #print("number_rating " + str(book.number_rating))
        book.save()

        serializer.save(book=book, review_user=review_user)


class ReviewList(generics.ListAPIView):
    serializer_class = serializers.ReviewSerializer
    #throttle_classes = [throttling.ReviewListThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(book=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = [permissions.IsReviewUserOrReadOnly]
    throttle_classes = [ScopedRateThrottle, AnonRateThrottle]
    throttle_scope = 'review-detail'


# class StreamPlatformVS(viewsets.ModelViewSet):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = serializers.StreamPlatformSerializer
#     permission_classes = [permissions.IsAdminOrReadOnly]
#     throttle_classes = [AnonRateThrottle]


class BookListAV(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    #throttle_classes = [AnonRateThrottle]

    def get(self, request):
        books = Book.objects.all()
        serializer = serializers.BookListSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.BookListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class BookDetailAV(APIView):
    permission_classes = [permissions.IsAdminOrReadOnly]
    #throttle_classes = [AnonRateThrottle]

    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.BookListSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = serializers.BookListSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)