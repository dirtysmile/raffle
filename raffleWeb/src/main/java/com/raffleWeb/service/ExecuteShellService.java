package com.raffleWeb.service;

import com.raffleWeb.config.AsyncConfig;
import com.raffleWeb.exec.ExecuteCmd;
import com.raffleWeb.exec.StreamGobbler;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import java.io.*;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.function.Consumer;
import java.util.stream.Stream;

@Service
@RequiredArgsConstructor
public class ExecuteShellService {

    private final ExecuteCmd executeCmd;

    @Async
    public void excute(String cmd){
        executeCmd.excute(cmd);
    }
}
