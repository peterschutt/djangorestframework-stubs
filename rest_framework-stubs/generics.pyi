from typing import Any, Dict, List, Optional, Sequence, Type, TypeVar, Union

from django.db.models import Manager, Model
from django.db.models.query import QuerySet
from rest_framework.filters import BaseFilterBackend
from rest_framework.pagination import BasePagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

from rest_framework import mixins, views

_T = TypeVar("_T", bound=Model)

def get_object_or_404(
    queryset: Union[Type[_T], Manager[_T], QuerySet[_T]], *filter_args: Any, **filter_kwargs: Any
) -> _T: ...

class GenericAPIView(views.APIView):
    queryset: Optional[QuerySet] = ...
    serializer_class: Optional[Type[BaseSerializer]] = ...
    lookup_field: str = ...
    lookup_url_kwarg: Optional[str] = ...

    filter_backends: Sequence[Type[BaseFilterBackend]] = ...
    pagination_class: Optional[Type[BasePagination]] = ...
    def get_queryset(self) -> QuerySet: ...
    def get_object(self) -> Any: ...
    def get_serializer(self, *args: Any, **kwargs: Any) -> BaseSerializer: ...
    def get_serializer_class(self) -> Type[BaseSerializer]: ...
    def get_serializer_context(self) -> Dict[str, Any]: ...
    def filter_queryset(self, queryset: QuerySet) -> QuerySet: ...
    @property
    def paginator(self) -> Optional[BasePagination]: ...
    def paginate_queryset(self, queryset: QuerySet) -> List[Any]: ...
    def get_paginated_response(self, data: Any) -> Response: ...

class CreateAPIView(mixins.CreateModelMixin, GenericAPIView):
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class ListAPIView(mixins.ListModelMixin, GenericAPIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class RetrieveAPIView(mixins.RetrieveModelMixin, GenericAPIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class DestroyAPIView(mixins.DestroyModelMixin, GenericAPIView):
    def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class UpdateAPIView(mixins.UpdateModelMixin, GenericAPIView):
    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...
    def patch(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class ListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class RetrieveUpdateAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericAPIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...
    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...
    def patch(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class RetrieveDestroyAPIView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...
    def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...

class RetrieveUpdateDestroyAPIView(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView
):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...
    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...
    def patch(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...
    def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response: ...