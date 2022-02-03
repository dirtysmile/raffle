package com.raffleWeb.controller;

import com.raffleWeb.config.QuartzTestConfig;
import com.raffleWeb.dto.AddSchedule;
import com.raffleWeb.dto.StopSchedule;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

@RestController
@RequiredArgsConstructor
@Slf4j
@RequestMapping("schedule")
public class ScheduleController {
    private final QuartzTestConfig quartzTestConfig;


    @GetMapping("/getMethod")
    public String test(){
        return "test";
    }

    @PostMapping("")
    public void registerSchdule(@RequestBody AddSchedule addSchedule){
        quartzTestConfig.register(addSchedule.getId());
    }

    @GetMapping("")
    public void getSchedule(){
        quartzTestConfig.scheduleList();
    }

    @PutMapping("/shutdown")
    public void shutdownSchedule(){
        quartzTestConfig.shotdown();
    }

    @PutMapping("/stop")
    public void stopSchedule(@RequestBody StopSchedule stopSchedule){
//        quartzTestConfig.stop(stopSchedule.getId());
        quartzTestConfig.stop(stopSchedule.getGrpName());

    }

//    @GetMapping("")
//    public String test2(){
//        log.info("test2 테스트 로그");
//        return "test2";
//    }

    @GetMapping("/test")
    public String test3(){
        return "test3";
    }
}
