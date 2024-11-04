package it.unipi.dsmt_2024_2025;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import it.unipi.dsmt_2024_2025.grpc.generated.GreeterGrpc;
import it.unipi.dsmt_2024_2025.grpc.generated.HelloReply;
import it.unipi.dsmt_2024_2025.grpc.generated.HelloRequest;

public class MainHelloClient {

    private final GreeterGrpc.GreeterBlockingStub blockingStub;

    public MainHelloClient(ManagedChannel channel) {
        blockingStub = GreeterGrpc.newBlockingStub(channel);
    }

    public String greet(String name) {
        HelloRequest request = HelloRequest.newBuilder().setName(name).build();
        HelloReply response;
        response = blockingStub.sayHello(request);
        return response.getMessage();
    }

    public static void main(String[] args) {
        String target = "[::]:8999";
        ManagedChannel channel = ManagedChannelBuilder.forTarget(target)
                .usePlaintext()
                .build();
        try {
            MainHelloClient client = new MainHelloClient(channel);
            String user = "world";
            String response = client.greet(user);
            System.out.println("Greeting: " + response);
        } finally {
            channel.shutdown();
        }
    }
}
