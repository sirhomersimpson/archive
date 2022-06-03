package com.udemy.dropbookmarks.resources;

import io.dropwizard.testing.junit.ResourceTestRule;
import org.junit.ClassRule;
import org.junit.Ignore;
import org.junit.Rule;
import org.junit.jupiter.api.Test;

import javax.ws.rs.core.MediaType;

import static org.junit.jupiter.api.Assertions.*;

public class HelloResourceTest {

    @ClassRule
    public static final ResourceTestRule RULE =
             ResourceTestRule.builder().addResource(new HelloResource()).build();
    @Test
    public void getValue() {
        System.out.println("skipped tests");
        String expected = "hello";
        String actual  = RULE
                .getJerseyTest()
                .client()
                .target("/testing")
                .request()
                .get(String.class);

    }

}