package com.redhat.training.examples;

public class Output {
    private String message;

    public Output() {}

    public Output(String message) {
        this.message = message;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    @Override
    public String toString() {
        return "Output{" +
                "message='" + message + '\'' +
                '}';
    }
}
