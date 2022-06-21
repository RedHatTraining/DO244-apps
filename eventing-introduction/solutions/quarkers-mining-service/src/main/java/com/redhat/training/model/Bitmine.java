package com.redhat.training.model;

import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;
import javax.persistence.Table;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

@Entity
@Table(name = "bitmine_quarkers")
public class Bitmine extends PanacheEntity {

    private String type;
    private Double weight;

    @Enumerated(EnumType.STRING)
    private BitmineStatus status;

    public String getType() {
        return type;
    }
    public void setType(String type) {
        this.type = type;
    }
    public Double getWeight() {
        return weight;
    }
    public void setWeight(Double weight) {
        this.weight = weight;
    }
    public BitmineStatus getStatus() {
        return status;
    }
    public void setStatus(BitmineStatus status) {
        this.status = status;
    }

    @Override
    public String toString() {
        return "Bitmine [status=" + status + ", type=" + type + ", weight=" + weight + "]";
    }

}
