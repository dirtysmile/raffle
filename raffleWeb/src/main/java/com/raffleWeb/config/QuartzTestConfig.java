package com.raffleWeb.config;

import com.raffleWeb.config.HelloJob;
import lombok.RequiredArgsConstructor;
import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;
import org.quartz.impl.matchers.GroupMatcher;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.quartz.SchedulerFactoryBean;
import org.springframework.stereotype.Service;

import javax.annotation.PostConstruct;
import java.util.Collections;
import java.util.Date;
import java.util.List;
import java.util.stream.Stream;

@Service
@RequiredArgsConstructor
public class QuartzTestConfig {
    private final SchedulerFactoryBean schedulerFactory;
    private final Scheduler scheduler;

    @PostConstruct
    public void scheduled() throws SchedulerException {
        JobDataMap map1 = new JobDataMap(Collections.singletonMap("cmd", "ls"));
        JobDataMap map2 = new JobDataMap(Collections.singletonMap("cmd", "ls"));
        JobDetail job1 = jobDetail("hello1", "hello-group", map1);
        JobDetail job2 = jobDetail("hello2", "hello-group", map2);
        SimpleTrigger trigger1 = trigger("trigger1", "trigger-group");
        SimpleTrigger trigger2 = trigger("trigger2", "trigger-group");
//        schedulerFactory.getObject().scheduleJob(job1, trigger1);
//        schedulerFactory.getObject().scheduleJob(job2, trigger2);


//        System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!");
//        System.out.println(scheduler.getJobGroupNames());
//        System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!");

    }

    public void register(int num){
        JobDataMap map = new JobDataMap(Collections.singletonMap("num", num));
        JobDetail job1 = jobDetail(Integer.toString(num), "hello-group2", map);
        SimpleTrigger trigger1 = trigger(Integer.toString(num), "trigger-group2");
        try{
            schedulerFactory.getObject().scheduleJob(job1, trigger1);
        }catch(SchedulerException e){

        }

    }

    public void scheduleList() {
        try{
            for (String groupName : scheduler.getJobGroupNames()) {

                for (JobKey jobKey : scheduler.getJobKeys(GroupMatcher.jobGroupEquals(groupName))) {

                    String jobName = jobKey.getName();
                    String jobGroup = jobKey.getGroup();

                    //get job's trigger
                    List<Trigger> triggers = (List<Trigger>) scheduler.getTriggersOfJob(jobKey);
                    Date nextFireTime = triggers.get(0).getNextFireTime();

                    System.out.println("[jobName] : " + jobName + " [groupName] : "
                            + jobGroup + " - " + nextFireTime);
                }

            }
        }catch(SchedulerException e){

        }
    }


    public void shotdown(){
        try{
            scheduler.shutdown();
        }catch(SchedulerException e){

        }

    }

    public void stop(String grpName){
        try{
            for (String groupName : scheduler.getJobGroupNames()) {

                if(!grpName.equals(groupName)){
                    continue;
                }
                System.out.println("!@#@!#!@#!@");
                System.out.println(groupName);
                System.out.println("!@#@!#!@#!@");
                for (JobKey jobKey : scheduler.getJobKeys(GroupMatcher.jobGroupEquals(groupName))) {

                    String jobName = jobKey.getName();
                    String jobGroup = jobKey.getGroup();

                    //get job's trigger
                    List<Trigger> triggers = (List<Trigger>) scheduler.getTriggersOfJob(jobKey);
                    Date nextFireTime = triggers.get(0).getNextFireTime();

                    scheduler.deleteJob(JobKey.jobKey(jobName,jobGroup));
                    System.out.println("[jobName] : " + jobName + " [groupName] : "
                            + jobGroup + " - " + nextFireTime);
                }

            }
        }catch(SchedulerException e){

        }
    }

    public void reRegister(){

    }


    public void restartJob(){

    }



    public void updateSchedule(){

    }

    public JobDetail jobDetail(String name, String group, JobDataMap dataMap) {
        JobDetail job = JobBuilder.newJob(RaffleJob.class)
                .withIdentity(name, group)
                .withDescription("simple hello job")
                .usingJobData(dataMap)
                .build();
        return job;
    }

    public SimpleTrigger trigger(String name, String group) {
        SimpleTrigger trigger = TriggerBuilder.newTrigger()
                .withIdentity(name, group)
                .withSchedule(SimpleScheduleBuilder.repeatSecondlyForever(10))
                .withDescription("hello my trigger")
                .build();
        return trigger;
    }


}
