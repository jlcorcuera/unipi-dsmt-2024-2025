package it.unipi.dsmt_2024_2025;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import it.unipi.dsmt_2024_2025.grpc.logic.GreeterImpl;

import java.io.IOException;

public class MainHelloServer {

    private static final int GRPC_SERVER_PORT = 8999;

    public static void main(String[] args) {
        try {
            Server server = ServerBuilder.forPort(GRPC_SERVER_PORT).addService(new GreeterImpl()).build();
            server.start();
            System.out.println("Server started at " + server.getPort());
            server.awaitTermination();
        } catch (IOException e) {
            System.out.println("Error: " + e);
        } catch (InterruptedException e) {
            System.out.println("Error: " + e);
        }
    }
}