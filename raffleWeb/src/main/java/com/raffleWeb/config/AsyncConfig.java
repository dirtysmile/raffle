package com.raffleWeb.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

import java.util.concurrent.Executor;

@Configuration
@EnableAsync
public class AsyncConfig {
    @Bean
    public Executor getAsyncExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(8);  // 대기 스레드 수
        executor.setMaxPoolSize(8); // 동시 동작하는, 최대 스레드
        executor.setQueueCapacity(500); // MaxPoolSize를 초과하는 요청이 Thread 생성 요청 시 해당 내용을 Queue에 저장하게 되고, 사용할 수 있는 Thread 여유 자리가 발생하면 하나씩 꺼내져서 동작하게 된다.
        executor.setThreadNamePrefix("seung-pool-");
        executor.initialize();
        return executor;
    }
}
