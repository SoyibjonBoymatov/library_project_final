from turtle import title


from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields=('id','title','author','content' , 'subtitle','isbn','price',)

    def validate(self, data):
        title=data.get('title',None)
        author=data.get('author',None)
        if not title.isalpha():
            raise ValidationError(
                {
                    "status":False,
                    "message":"Make it in str not int"
                }
            )


        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    "status":False,
                    "message":"Book with this title already exists"
                }
            )

        return data

    def validate_price(self,price):
        if price < 0 or price > 99999999:
            raise ValidationError(
                {
                    "status":False,
                    "message":"price input is wrong"
                }
            )
