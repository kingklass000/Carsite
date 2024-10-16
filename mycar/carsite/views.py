from rest_framework import viewsets, permissions, generics, status
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import CheckOwner


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user = serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializers.validated_data
        return Response(serializers.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CarListViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['car_name']
    ordering_fields = ['price', 'year']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CarDetailViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]

    def perform_create(self, serializer):
        serializer.save(owmer=self.request.user)


class ProductPhotosViewSet(viewsets.ModelViewSet):
    queryset = CarPhotos.objects.all()
    serializer_class = CarPhotosSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CarPhotosViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = CarPhotosSerializer
