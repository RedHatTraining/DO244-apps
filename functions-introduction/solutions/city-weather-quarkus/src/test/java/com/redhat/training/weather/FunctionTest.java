package com.redhat.training.weather;

import io.quarkus.test.junit.QuarkusTest;
import io.restassured.RestAssured;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import static org.hamcrest.Matchers.equalTo;

@QuarkusTest
public class FunctionTest {

    @Test
    void testFunction() throws Exception {
        Output output = ( new Function() ).function( new Input( "kathmandu" ) );
        Assertions.assertEquals( "{\"city\":\"kathmandu\",\"temperature\":{\"kelvin\":291.15,\"celsius\":18.0,\"fahrenheit\":64.39999999999992}}",
                output.getMessage().toString() );
    }

    @Test
    void testCityNotFoundFunction() throws Exception {
        Output output = ( new Function() ).function( new Input( "israel" ) );
        Assertions.assertEquals( "{\"city\":\"israel\",\"message\":\"City cannot be found!!\"}", output.getMessage().toString() );
    }

    @Test
    public void testFunctionIntegration() {
        RestAssured.given()
                .queryParam( "city", "kathmandu" )
                .when()
                .get( "/" )
                .then()
                .statusCode( 200 )
                .body(
                        "message",
                        equalTo( "{\"city\":\"kathmandu\",\"temperature\":{\"kelvin\":291.15,\"celsius\":18.0,\"fahrenheit\":64.39999999999992}}" ) );
    }

    @Test
    public void testCityNotFoundFunctionIntegration() {
        RestAssured.given()
                .queryParam( "city", "israel" )
                .when()
                .get( "/" )
                .then()
                .statusCode( 200 )
                .body( "message", equalTo( "{\"city\":\"israel\",\"message\":\"City cannot be found!!\"}" ) );
    }

}
