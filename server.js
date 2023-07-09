const PROTO_PATH = "./customers.proto";

var grpc = require("grpc");
var protoLoader = require("@grpc/proto-loader");

//먼저, customers.proto 파일을 protoLoader를 사용하여 JavaScript 객체로 변환
var packageDefinition = protoLoader.loadSync(PROTO_PATH, {
    keepCase: true,
    longs: String,
    enums: String,
    arrays: true
});


//grpc.loadPackageDefinition() 함수를 사용하여 패키지 정의 객체를 생성합니다.
var customersProto = grpc.loadPackageDefinition(packageDefinition);

const { v4: uuidv4 } = require("uuid");

const server = new grpc.Server();
const customers = [
    {
        id: "아이디1",
        name: "이름1",
        age: 19,
        address: "Address 1"
    },
    {
        id: "아이디2",
        name: "이름2",
        age: 19,
        address: "Address 2"
    }
];

//server.addService() 함수를 사용하여 서비스와 메소드를 서버에 추가합니다. (proto 파일에 정의한 것.)
server.addService(customersProto.CustomerService.service, {
    getAll: (_, callback) => {
        callback(null, { customers });
    },

    get: (call, callback) => {
      //call.request는 서버에서 받은 요청 메시지를 나타내는 객체
        let customer = customers.find(n => n.id == call.request.id);
        if (customer) {
            callback(null, customer);
        } else {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "Not found !"
            });
        }
    },

    insert: (call, callback) => {
        let customer = call.request;
        
        customer.id = uuidv4();
        customers.push(customer);
        callback(null, customer);
    },

    update: (call, callback) => {
        let existingCustomer = customers.find(n => n.id == call.request.id);

        if (existingCustomer) {
            existingCustomer.name = call.request.name;
            existingCustomer.age = call.request.age;
            existingCustomer.address = call.request.address;
            callback(null, existingCustomer);
        } else {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "Not found"
            });
        }
    },

    remove: (call, callback) => {
        let existingCustomerIndex = customers.findIndex(
            n => n.id == call.request.id
        );

        if (existingCustomerIndex != -1) {
            customers.splice(existingCustomerIndex, 1);
            callback(null, {});
        } else {
            callback({
                code: grpc.status.NOT_FOUND,
                details: "Not found"
            });
        }
    }
});

server.bind("127.0.0.1:30043", grpc.ServerCredentials.createInsecure());
console.log("Server running at http://127.0.0.1:30043");
server.start();