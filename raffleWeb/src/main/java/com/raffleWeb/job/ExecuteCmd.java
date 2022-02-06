package com.raffleWeb.job;

import com.google.gson.JsonArray;
import com.google.gson.JsonParser;
import org.json.JSONArray;
import org.json.JSONObject;
import org.springframework.stereotype.Service;

import java.io.*;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;

@Service
public class ExecuteCmd {
    private final String USER_HOME = System.getProperty("user.home");
    private final String USER_DIR = System.getProperty("user.dir");

    public void excute(String cmd){
        String list = "";

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
                list = line;
            }

            JSONArray jsonArray = new JSONArray(list);

            for (int i = 0; i < jsonArray.length(); i++)
            {
                JSONObject jsonObj = jsonArray.getJSONObject(i);

                System.out.println(jsonObj);
            }

//            JsonParser jsonParser = new JsonParser();
//            JsonArray jsonArray = (JsonArray)jsonParser.parse(list);


            List<String> eomi_list = Arrays.asList(list);

            System.out.println(eomi_list.get(0));


            int exitCode = process.waitFor();
        }catch(IOException e){
            e.printStackTrace();
        }catch(InterruptedException e){
            e.printStackTrace();
        }
    }
}
