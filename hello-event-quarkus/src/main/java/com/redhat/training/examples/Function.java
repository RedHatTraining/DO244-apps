package com.redhat.training.examples;



import javax.inject.Inject;

import org.jboss.logging.Logger;

import io.quarkus.funqy.Funq;
import io.quarkus.funqy.knative.events.CloudEvent;
import io.quarkus.funqy.knative.events.CloudEventBuilder;


public class Function 
{

    @Inject
    Logger logger;

    @Funq
    public CloudEvent<Output> function(CloudEvent<Input> input) 
    {
        //System.out.println(input);
        logger.infof("New event is: %s", input );
        Output output = new Output(input.data().getMessage());
        CloudEvent<Output> outputCloudEvent = CloudEventBuilder.create().build(output);
        return outputCloudEvent;
    }

}
