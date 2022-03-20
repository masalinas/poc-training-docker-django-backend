from rest_framework import serializers
from django.utils.encoding import smart_str

from bson import ObjectId
from bson.errors import InvalidId

from ApiApplication.models import Product

class ObjectIdField(serializers.Field):
    """ Serializer field for Djongo ObjectID fields """
    def to_internal_value(self, data):
        # Serialized value -> Database value
        try:
            # Get the ID, then build an ObjectID instance using it
            return ObjectId(str(data))
        except InvalidId:
            raise serializers.ValidationError(
                '`{}` is not a valid ObjectID'.format(data))

    def to_representation(self, value):
        # Database value -> Serialized value
        # User submitted ID's might not be properly structured
        if not ObjectId.is_valid(value):
            raise InvalidId

        return smart_str(value)
...

class ProductSerializer(serializers.ModelSerializer):

    id = ObjectIdField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
