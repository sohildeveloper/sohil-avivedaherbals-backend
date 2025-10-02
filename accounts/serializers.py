from rest_framework import serializers   # DRF's tool for converting JSON ↔ Python objects
from .models import User                 # Import our custom User model
from django.contrib.auth.hashers import make_password, check_password   # For hashing passwords

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Serializer = like a translator between JSON request and Django model
    
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

        extra_kwargs = {
            'password': {'write_only': True}  # don’t return password in API response
        }
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        # make_password = securely hash the password (instead of plain text)
        return super().create(validated_data)

class UserLoginSerializer(serializers.Serializer):
    # Not tied to model directly (because login only needs email + password input)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)  # Find user by email
        except User.DoesNotExist:
            raise serializers.ValidationError({"error": "Invalid email or password"})

        if not check_password(password, user.password):  
            # Compare entered password with hashed one in DB
            raise serializers.ValidationError({"error": "Invalid email or password"})

        data['user'] = user  # Attach user object for later use
        return data