package com.redhat.training.service;

import javax.enterprise.context.ApplicationScoped;
import javax.transaction.Transactional;

import com.redhat.training.model.Bitmine;
import com.redhat.training.model.BitmineStatus;

@ApplicationScoped
public class MiningService {

    public Bitmine process(Bitmine bitmine){
        bitmine.setStatus(BitmineStatus.PROCESSED);
        return bitmine;
    }

    @Transactional
    public void store(Bitmine bitmine){
        bitmine.persist();
    }
    
}
