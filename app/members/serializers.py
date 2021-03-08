from rest_framework import serializers

from members.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # get에 password 보이지 않게
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['pk', 'username', 'password', 'name', 'age', 'gender']

    def save(self, **kwargs):
        username = self.validated_data['username']
        password = self.validated_data['password']
        name = self.validated_data['name']
        age = self.validated_data['age']
        gender = self.validated_data['gender']

        user = User.objects.create_user(
            username=username,
            password=password,
            name=name,
            age=age,
            gender=gender,
        )
        return user
