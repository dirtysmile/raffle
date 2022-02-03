package com.raffleWeb;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


@Slf4j
@SpringBootApplication
public class RaffleWebApplication {

	public static void main(String[] args) {
		SpringApplication.run(RaffleWebApplication.class, args);
		log.trace("Hi I'm {} log", "TRACE");
		log.debug("Hi I'm {} log", "DEBUG");
		log.info("Hi I'm {} log", "INFO");
		log.warn("Hi I'm {} log", "WARN");
		log.error("Hi I'm {} log", "ERROR");

	}

}
