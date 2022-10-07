from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform


# ModelSerializer - zawiera wszystkie metody ktore ma serializer np. get, create itp

class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField() #do obliczania dlugosci nazwy filmu oraz innych parametrow mozna
     class Meta:
          model = WatchList
          fields = "__all__"
         # fields = "__all__" # ['id', 'name', 'description']
         # exclude = ['name']



class StreamPlatformSerializer(serializers.ModelSerializer):
    #watchlist = WatchListSerializer(many=True, read_only=True) #nested serializer wyswietla calosc danych
    #watchlist = serializers.StringRelatedField(many=True) #zwraca name
    #watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    watchlist = serializers.HyperlinkedRelatedField( # dodajemy do views serializer context={'request': request}
        many=True,
        read_only=True,
        view_name='movie_detail' #bierzemy z urls
    )

    class Meta:
        model = StreamPlatform
        fields = "__all__"

#(serializers.Serializer)
# validators
# def name_length(value):
#      if len(value) < 2:
#           raise serializers.ValidationError('name is to short')
#
#
# class MovieSerializer(serializers.Serializer):
#      id = serializers.IntegerField(read_only=True)
#      #name = serializers.CharField() to jest do field validation
#      name = serializers.CharField(validators=[name_length]) #validators
#      description = serializers.CharField()
#      active = serializers.BooleanField()
#
#      def create(self, validated_data):
#           return Movie.objects.create(**validated_data)
#
#      def update(self, instance, validated_data):
#           instance.name = validated_data.get('name', instance.name)
#           instance.description = validated_data.get('description', instance.description)
#           instance.active = validated_data.get('active', instance.active)
#           instance.save()
#           return instance

     # FIELD LVL VALIDATION   sprawdzanie warunku dla wybranego pola
     # def validate_name(self, value): # sprawdza dlugosci dla name
     #      if len(value) < 2:
     #           raise serializers.ValidationError("name is to short")
     #      else:
     #           return value

     # Object level validation SPRAWDZANIE WARUNKU DLA OBIEKTU
     # def validate(self, data):
     #      if data['name'] == data['description']:
     #            raise serializers.ValidationError("title and descr should be other")
     #      else:
     #           return data