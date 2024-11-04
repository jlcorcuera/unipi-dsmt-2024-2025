package it.unipi.dsmt_2024_2025.grpc.logic;

import io.grpc.stub.StreamObserver;
import it.unipi.dsmt_2024_2025.grpc.generated.GreeterGrpc;
import it.unipi.dsmt_2024_2025.grpc.generated.HelloReply;
import it.unipi.dsmt_2024_2025.grpc.generated.HelloRequest;


public class GreeterImpl extends GreeterGrpc.GreeterImplBase {
    /*
     * We observe here that some words have an @, these are Annotations.
     * Annotations are used to provide supplement information about a program. We can autogenerate this functions,
     * in Intellij we can use the shortcut ctrl + O to do this.
     * */
    @Override
    public void sayHello(HelloRequest request, StreamObserver<HelloReply> responseObserver) {
        /* Build a response composed with the constant Hello and the name variable from the request.
         * For example, if the request is: gRPC the reply will be: "Hello gRPC".
         */
        HelloReply reply = HelloReply.newBuilder().setMessage("Hello " + request.getName() + " from Java!.").build();
        responseObserver.onNext(reply);
        /* We use the response observer's onCompleted method to specify that we've finished dealing with the RPC */
        responseObserver.onCompleted();
    }

    public void sayHelloAgain(HelloRequest request,
                              StreamObserver<HelloReply> responseObserver) {
        /* Build a response composed with the constant Hello and the name variable from the request.
         * For example, if the request is: gRPC the reply will be: "Hello gRPC".
         */
        HelloReply reply = HelloReply.newBuilder().setMessage("Hello " + request.getName() + " from HelloAgainJava!").build();
        responseObserver.onNext(reply);
        /* We use the response observer's onCompleted method to specify that we've finished dealing with the RPC */
        responseObserver.onCompleted();
    }
}
