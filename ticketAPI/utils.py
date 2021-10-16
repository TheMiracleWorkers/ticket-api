from api.serializers import CurrentUserSerializer


def jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': CurrentUserSerializer(user, context={'request': request}).data
    }
