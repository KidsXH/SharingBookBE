from rest_framework import status
from rest_framework.response import Response


class ResponseMsg:
    @staticmethod
    def ok(msg=None):
        return Response({'message': msg}, status=status.HTTP_200_OK)

    @staticmethod
    def created(msg=None):
        return Response({'message': msg}, status=status.HTTP_201_CREATED)

    @staticmethod
    def bad_request(msg=None):
        return Response({'message': msg}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def unauthorized(msg=None):
        return Response({'message': msg}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def forbidden(msg=None):
        return Response({'message': msg}, status=status.HTTP_403_FORBIDDEN)

    @staticmethod
    def not_found(msg=None):
        return Response({'message': msg}, status=status.HTTP_404_NOT_FOUND)




