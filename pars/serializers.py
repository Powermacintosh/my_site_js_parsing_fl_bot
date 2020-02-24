from rest_framework.serializers import ModelSerializer
from .models import Fl


class Serializer(ModelSerializer):

	class Meta:
		model = Fl
		fields = ['id', 'link', 'show', 'ref_link', 'price', 'date_p', 'time_p']