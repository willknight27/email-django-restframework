from rest_framework import serializers

# Serializer para validacion de campos JSON de formulario de contacto
class EmailSerializer(serializers.Serializer):

    subject = serializers.CharField(max_length=200)
    message = serializers.CharField(max_length=200)
    message_email = serializers.EmailField(max_length=250)

    def validate(self, data):
        return data