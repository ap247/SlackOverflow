from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Comment
from .serializers import CommentSerializer

# Create your views here.

#get all comments
@api_view(['GET'])
def getComments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

#get single comment
@api_view(['GET'])
def getComment(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comment, many=False)
    return Response(serializer.data)

#add comment
@api_view(['POST'])
def addComment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#update comment
@api_view(['PUT'])
def updateComment(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete comment
@api_view(['DELETE'])
def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    
    return Response('Comment successfully deleted!')