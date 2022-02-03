package com.raffleWeb.test;

import java.io.File;
import java.io.IOException;

public class Test {
    public static void main(String[] args)throws IOException, InterruptedException {
        ProcessBuilder builder = new ProcessBuilder();
        builder.command("sh","-c","mkdir /tmp/test");
        builder.directory(new File(System.getProperty("user.home")));

        var process = builder.start();


        var ret = process.waitFor();

        System.out.printf("Program exited with code: %d", ret);
    }
}
