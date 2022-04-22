from rest_framework import serializers
from CryptoApi.models.models import TradingStrategy, Coin, Pattern


class StrategySerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField('_user')
    coins = serializers.PrimaryKeyRelatedField(queryset=Coin.objects.all(), many=True)
    pattern = serializers.PrimaryKeyRelatedField(queryset=Pattern.objects.all(), many=True)

    class Meta:
        model = TradingStrategy
        fields = ('user', 'coins', 'patterns')

    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return request.user

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        strategy = TradingStrategy.objects.create(
            user=validated_data["user"],
            coins=validated_data["coins"],
            pattren=validated_data["patterns"]
        )
        strategy.save()

        return strategy
