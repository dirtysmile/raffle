package com.raffleWeb.service;

import com.raffleWeb.config.QuartzTestConfig;
import com.raffleWeb.repository.ScheduleRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ScheduleService {
    private final QuartzTestConfig quartzTestConfig;
    private final ScheduleRepository scheduleRepository;

    public void registerSchedule(int num){
        scheduleRepository.register(num);
        quartzTestConfig.register(num);
    }
}
