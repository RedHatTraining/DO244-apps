package com.redhat.training;

import io.quarkus.test.junit.NativeImageTest;

@NativeImageTest
public class NativeLoggerResourceIT extends LoggerResourceTest {

    // Execute the same tests but in native mode.
}