package functions;

import io.quarkus.test.junit.QuarkusTest;
import io.restassured.RestAssured;
//import org.hamcrest.CoreMatchers;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import static org.hamcrest.Matchers.equalTo;
//import static org.hamcrest.Matchers.notNullValue;

@QuarkusTest
public class FunctionTest {

    @Test
    void testFunction() throws Exception {
        Output output = (new Function()).function(new Input("kathmandu"));
        Assertions.assertEquals("{\"city\":\"kathmandu\",\"temperature\":{\"kelvin\":291.15,\"celsius\":18.0,\"fahrenheit\":64.39999999999992}}", output.getMessage().toString());
    }

    @Test
    public void testFunctionIntegration() {
        RestAssured.given().contentType("application/json")
                .body("{\"message\": \"kathmandu\"}")
                .header("ce-id", "42")
                .header("ce-specversion", "1.0")
                .post("/")
                .then().statusCode(200)
                .body("message", equalTo("{\"city\":\"kathmandu\",\"temperature\":{\"kelvin\":291.15,\"celsius\":18.0,\"fahrenheit\":64.39999999999992}}"));
    }

}
