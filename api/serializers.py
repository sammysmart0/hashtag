from rest_framework import serializers
from hashuser.models import CustomUser


class Customserializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
        # (
        #     'id',
        #     'email',    
        #     'username',
        #     'password',
        #     'first_name',
        #     'last_name',
        #     'date_of_birth',
        #     'gender',
        #     'phone_number',
        #     'matric_number',
        #     'department',
        # )