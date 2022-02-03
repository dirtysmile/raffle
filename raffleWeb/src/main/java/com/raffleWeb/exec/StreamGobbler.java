package com.raffleWeb.exec;

import java.io.*;
import java.util.function.Consumer;
import java.util.stream.Stream;

public class StreamGobbler implements Runnable{
    private InputStream inputStream;
    private Consumer<String> consumer;


    public StreamGobbler(InputStream inputStream, Consumer<String> consumer) {
        this.inputStream = inputStream;
        this.consumer = consumer;
    }


    @Override
    public void run() {
        String s;
        try{
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream, "euc-kr"));
//            Stream<String> lines = bufferedReader.lines();
//            while ((s=bufferedReader.readLine()) !=null){
//                System.out.println(s);
//            }

//            new BufferedReader(new InputStreamReader(inputStream, "euc-kr")).lines().forEach(consumer);
        }catch (UnsupportedEncodingException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }

    }
}
