from rest_framework import serializers
from watchlist_app.models import Movie


# validators
def name_length(value):
     if len(value) < 2:
          raise serializers.ValidationError('name is to short')


class MovieSerializer(serializers.Serializer):
     id = serializers.IntegerField(read_only=True)
     #name = serializers.CharField() to jest do field validation
     name = serializers.CharField(validators=[name_length])
     description = serializers.CharField()
     active = serializers.BooleanField()

     def create(self, validated_data):
          return Movie.objects.create(**validated_data)

     def update(self, instance, validated_data):
          instance.name = validated_data.get('name', instance.name)
          instance.description = validated_data.get('description', instance.description)
          instance.active = validated_data.get('active', instance.active)
          instance.save()
          return instance

     # FIELD LVL VALIDATION   sprawdzanie warunku dla wybranego pola
     # def validate_name(self, value): # sprawdza dlugosci dla name
     #      if len(value) < 2:
     #           raise serializers.ValidationError("name is to short")
     #      else:
     #           return value

     # Object level validation SPRAWDZANIE WARUNKU DLA OBIEKTU
     def validate(self, data):
          if data['name'] == data['description']:
                raise serializers.ValidationError("title and descr should be other")
          else:
               return data