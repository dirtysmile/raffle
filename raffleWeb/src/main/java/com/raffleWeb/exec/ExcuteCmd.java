package com.raffleWeb.exec;

public abstract class ExcuteCmd implements Excuteable{
    private final String USER_HOME = System.getProperty("user.home");
    private final String USER_DIR = System.getProperty("user.dir");

    @Override
    public void excute(String cmd) {
        String list = "";

        boolean isWindows = System.getProperty("os.name").toLowerCase().startsWith("windows");

        ProcessBuilder builder = new ProcessBuilder();

        if(isWindows){
            builder.command("cmd.exe","/c","dir");
        }else{
            builder.command("sh","-c",cmd);
        }


        afterJob();
    }
}
