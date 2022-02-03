package com.raffleWeb.service;

import com.raffleWeb.config.QuartzTestConfig;
import com.raffleWeb.repository.ScheduleRepository;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.*;
import org.mockito.junit.jupiter.MockitoExtension;
import org.mockito.junit.jupiter.MockitoSettings;
import org.mockito.quality.Strictness;

import java.util.HashMap;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.*;

@ExtendWith(MockitoExtension.class)
@MockitoSettings(strictness = Strictness.LENIENT)
class ScheduleServiceTest {

    @InjectMocks
    private ScheduleService scheduleService;

    @Mock
    private ScheduleRepository scheduleRepository;

    @Mock
    private QuartzTestConfig quartzTestConfig;


    @Test
    void test(){
        System.out.println("test");
        Assertions.assertTrue(true);
    }

    @Test
    void test2() throws Exception{

        //given

        //when
        Mockito.doReturn(1).when(scheduleRepository).register(ArgumentMatchers.anyInt());
        Mockito.doNothing().when(quartzTestConfig).register(ArgumentMatchers.anyInt());
        //then


        Thread.sleep(5000);
        scheduleService.registerSchedule(1);
        quartzTestConfig.scheduleList();

        Thread.sleep(5000);
    }


    @Test
    void test3(){
        Object a = "string";
        Object b = new HashMap<String,Object>();

        System.out.println(a.getClass().equals(String.class));
        System.out.println(b.getClass().equals(HashMap.class));
    }

}