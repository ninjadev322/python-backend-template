from alvinchow_service_protobuf import alvinchow_service_pb2_grpc, common_pb2
from alvinchow_service.api.grpc import serializers
from alvinchow_service.api.grpc.request import handle_grpc_errors
from alvinchow_service.lib import get_logger


from alvinchow.lib.dates import utcnow


logger = get_logger(__name__)


class Foo:
    pass


class AlvinChowServiceServicer(alvinchow_service_pb2_grpc.AlvinChowServiceServicer):

    @handle_grpc_errors()
    def GetFoo(self, request, context):
        foo = Foo()
        foo.id = request.id
        foo.created_at = utcnow()
        foo.name = 'Foo'

        return serializers.serialize_foo(foo)

    @handle_grpc_errors()
    def Ping(self, request, context):
        return common_pb2.SimpleResponse(success=True)
