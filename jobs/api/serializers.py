from rest_framework import serializers
from jobs.models import JobOffer

# Serializerとは、クエリセットやモデルインスタンスのような複雑なデータをJson形式のフォーマットに変換する
class JobOfferSerializer(serializers.ModelSerializer):
  class Meta:
    model = JobOffer
    fields = '__all__'