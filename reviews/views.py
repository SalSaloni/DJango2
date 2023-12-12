from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review

# Create your views here.
class AppDevClubReviewsView(APIView):
    def get(self, request):
        reviews = []
        for review in Review.objects.filter():
            reviews.append(review.name_text),
            reviews.append(review.email_text),
            reviews.append(review.phone_text),
            reviews.append(review.review_text),
            
        reviews = list(filter(None, reviews))
        reviews = list(set(reviews))
        return Response({'reviews': reviews})

class CreateAppDevClubReview(APIView):
    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        phone = request.data['phone']
        review = request.data['review']
        if name != '':
            new_database_entry = Review(name_text=name)
        if email != '':
            new_database_entry = Review(email_text=email)
        if phone != '':
            new_database_entry = Review(phone_text=phone)
        if name != '':
            new_database_entry = Review(review_text=review)

            new_database_entry.save()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'failure'})
