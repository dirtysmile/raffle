package com.raffleWeb.exec;

public abstract class ABtest implements ExcuteShell{
    @Override
    public void execute(String cmd) {
        System.out.println("test A");
        after();
    }
}
