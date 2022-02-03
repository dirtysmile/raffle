package com.raffleWeb.exec;

import org.springframework.stereotype.Service;

import java.io.*;
import java.util.stream.IntStream;

@Service
public class ExecuteCmd {
    private final String USER_HOME = System.getProperty("user.home");
    private final String USER_DIR = System.getProperty("user.dir");


    public void excute(String cmd){
        System.out.println(USER_HOME);
        System.out.println(USER_DIR);

        boolean isWindows = System.getProperty("os.name").toLowerCase().startsWith("windows");

        ProcessBuilder builder = new ProcessBuilder();

        if(isWindows){
            builder.command("cmd.exe","/c","dir");
        }else{
            builder.command("sh","-c",cmd);
        }

        builder.directory(new File(System.getProperty("user.home")));
        String line;

        try{
            Process process = builder.start();
            InputStream stdout = process.getInputStream ();
            BufferedReader reader = new BufferedReader (new InputStreamReader(stdout));
            while ((line = reader.readLine ()) != null) {
                System.out.println ("Stdout: " + line);
            }

            int exitCode = process.waitFor();
            System.out.println(exitCode);
        }catch(IOException e){
            e.printStackTrace();
        }catch(InterruptedException e){
            e.printStackTrace();
        }
    }
}
