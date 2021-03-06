package com.redhat.training.examples;

public class Input {
    private String message;

    public Input() {}

    public Input(String message) {
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
        return "Input{" +
                "message='" + message + '\'' +
                '}';
    }
}
