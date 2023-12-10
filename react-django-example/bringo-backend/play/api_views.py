from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import permissions
from play.serializer import BoardSerializer
from play.models import Board
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache

class BoardList(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id','owner')

class BoardCreate(CreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        try:
            name = request.data.get('name')
        except:
            raise ValidationError({'name': 'please enter a title for the board'})
        
        return super().create(request, *args, **kwargs)

class BoardRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    lookup_field = 'id'
    serializer_class = BoardSerializer

    def delete(self, request, *args, **kwargs):
        # board_id = request.data.get('id')
        
        try:
            auth = Board.objects.get(id=request.data['board_id']).owner == request.data['token']
        except:
            auth = False

        if auth:
            response = super().delete(request, *args, **kwargs)
            # if response.status_code == 204:
            #     cache.delete(f'board_data_{board_id}')
            return response
    
        else:
            return Response({'status_code': 403, 'error': 'incorrect user'})

    def update(self, request, *args, **kwargs):

        try:
            auth = Board.objects.get(id=request.data['board_id']).owner == request.data['owner']
        except:
            auth = False

        if auth:
            response = super().update(request, *args, **kwargs)
            if response.status_code == 200:
                board = response.data # i dunno if any of this works
                cache.set(f"board_data_{board['id']}", {
                    'name': board['name'],
                    'tiles': board['tiles']
                })
            return response
        
        else:
            return Response({'status_code': 403, 'error': 'incorrect user'})