package com.redhat.training.rest;

import java.util.logging.Logger;

import javax.inject.Inject;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.HttpHeaders;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.Status;

import com.redhat.training.model.Bitmine;
import com.redhat.training.service.MiningService;

@Path("/")
public class MiningResource {

        private static final Logger LOGGER = Logger.getLogger("mining-resource");

        @Inject
        private MiningService miningService;

        // TODO: Create a method called "process" to handle the bitmine cloudevents
        @POST
        @Path("/")
        public Response process(@Context HttpHeaders httpHeaders, Bitmine bitmine) {

                logHeaders(httpHeaders);

                miningService.process(bitmine);

                LOGGER.info("Processed Bitmine:" + bitmine.toString());

                miningService.store(bitmine);

                LOGGER.info("Bitmine is stored in the DB");

                return Response.status(Status.OK).entity("{\"status\":\"successful\"}")
                                .build();
        }

        private void logHeaders(HttpHeaders httpHeaders) {
                LOGGER.info("Cloud Event:");

                LOGGER.info("ce-id=" + httpHeaders.getHeaderString("ce-id"));
                LOGGER.info(
                                "ce-source=" + httpHeaders.getHeaderString("ce-source"));
                LOGGER.info("ce-specversion="
                                + httpHeaders.getHeaderString("ce-specversion"));
                LOGGER.info("ce-time=" + httpHeaders.getHeaderString("ce-time"));
                LOGGER.info("ce-type=" + httpHeaders.getHeaderString("ce-type"));
                LOGGER.info(
                                "content-type=" + httpHeaders.getHeaderString("content-type"));
                LOGGER.info("content-length="
                                + httpHeaders.getHeaderString("content-length"));
        }

}
