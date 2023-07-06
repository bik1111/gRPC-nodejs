const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

// 프로토를 JavaScript 객체로 전환하기 위해서는 먼저 패키지 정의를 설정해야 합니다. 
// protoLoader는 첫 번째 매개변수로 프로토 파일이 위치한 경로를 받고, 두 번째로 설정 속성을 받아 이 작업을 처리합니다.
const packageDefinition = protoLoader.loadSync('customers.proto', {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
});

//패키지 정의 객체를 손에 넣으면, 이를 grpc 객체의 loadPackageDefinition 함수에 전달하여 반환받을 수 있습니다.
// 클라이언트 생성 위함.
const CustomerService = grpc.loadPackageDefinition(packageDefinition).CustomerService;
//클라이언트 생성
const client = new CustomerService(
  "localhost:30043",
  grpc.credentials.createInsecure()
);


module.exports = client;
