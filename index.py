from flask import Flask, jsonify
import client
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # gRPC 클라이언트 생성
    client_instance = client.create_client()

    # 서버에 요청 보내기
    response = client_instance.GetAll(client.Empty())

    # 응답 처리
    customers = response.customers # RepeatedCompositeContainer를 리스트로 변환
    
    customers_serializable = []

    for customer in customers:
        customer_dict = {
            "id": customer.id,
            "name": customer.name,
            "age": customer.age,
            "address": customer.address
        }
        customers_serializable.append(customer_dict)

    # JSON 인코딩 시 ensure_ascii=False로 설정하여 유니코드 문자를 보존
    json_data = json.dumps(customers_serializable, ensure_ascii=False).encode('utf-8')    
    return json_data, 200, {'Content-Type': 'application/json; charset=utf-8'}


if __name__ == "__main__":
    app.run(debug=True, port=4000)
