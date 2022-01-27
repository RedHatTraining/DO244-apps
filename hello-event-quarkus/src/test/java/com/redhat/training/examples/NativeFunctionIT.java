package com.redhat.training.examples;

import org.junit.jupiter.api.Test;
//import static io.restassured.RestAssured.given;
//import static org.hamcrest.CoreMatchers.is;
import io.quarkus.test.junit.NativeImageTest;
import io.restassured.RestAssured;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.notNullValue;

@NativeImageTest
public class NativeFunctionIT extends FunctionTest 
{

    // Execute the same tests but in native mode.
    @Test
    public void testFunctionIntegrationNative() {
        RestAssured.given().contentType("application/json")
                .body("{\"message\": \"Hello!\"}")
                .header("ce-id", "42")
                .header("ce-specversion", "1.0")
                .post("/")
                .then().statusCode(200)
                .header("ce-id", notNullValue())
                .header("ce-specversion", equalTo("1.0"))
                .header("ce-source", equalTo("function"))
                .header("ce-type", equalTo("function.output"))
                .body("message", equalTo("Hello!"));
    }
}
