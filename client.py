import grpc
from grpc import insecure_channel
from customers_pb2 import Empty, Customer, CustomerList, CustomerRequestId
from customers_pb2_grpc import CustomerServiceStub

# gRPC 서버에 연결
channel = insecure_channel("localhost:30043")
stub = CustomerServiceStub(channel)

# 클라이언트 생성
def create_client():
    return stub

# 이하의 코드는 필요한 클라이언트 함수들을 호출하는 예시입니다.
if __name__ == "__main__":
    client = create_client()
    response = client.GetAll(Empty())
    print(response)



