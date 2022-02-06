package com.raffleWeb.service;

import com.raffleWeb.job.ExecuteCmd;
import lombok.RequiredArgsConstructor;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ExecuteShellService {

    private final ExecuteCmd executeCmd;

    @Async
    public void excute(String cmd){
        executeCmd.excute(cmd);
    }
}
