package org.acme;

import org.junit.jupiter.api.Test;
import io.quarkus.test.junit.NativeImageTest;
import static io.restassured.RestAssured.given;
import static org.hamcrest.CoreMatchers.is;

@NativeImageTest
public class NativeGreetingResourceIT extends GreetingResourceTest {
    // Execute the same tests but in native mode.
    @Test
    public void testHelloEndpointNative()
    {
        given()
        .when().get("/hello")
        .then()
           .statusCode(200)
           .body(is("Hello World"));
    }

   
}