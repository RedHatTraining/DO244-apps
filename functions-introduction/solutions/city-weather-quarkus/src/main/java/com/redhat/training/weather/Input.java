package com.redhat.training.weather;

public class Input {
    String city;

    public Input() {}

    public Input(String city) {
        this.city = city;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
}
