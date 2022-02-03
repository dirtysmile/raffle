package com.raffleWeb.config;

import com.raffleWeb.exec.ExecuteCmd;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.quartz.Job;
import org.quartz.JobDataMap;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;
import org.springframework.beans.factory.annotation.Autowired;

@Slf4j
@RequiredArgsConstructor
public class HelloJob implements Job {
    private final ExecuteCmd executeCmd;

    @Override
    public void execute(JobExecutionContext context) throws JobExecutionException {
        JobDataMap map = context.getJobDetail().getJobDataMap();
        log.info("RequestContractJob execute invoked, job-detail-key:{}, fired-time:{}, num:{}",
                context.getJobDetail().getKey(), context.getFireTime(), map.getInt("num"));
        log.info("RequestContractJob execute complete");
        afterExecute(context);
    }

    private void afterExecute(JobExecutionContext context) {
        log.info("%%% After executing job");
    }
}
