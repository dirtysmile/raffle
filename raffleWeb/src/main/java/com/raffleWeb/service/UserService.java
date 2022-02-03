package com.raffleWeb.service;

import com.raffleWeb.dto.SignUpDTO;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserService {

    private final TestService1 testService1;

    public boolean isEmailExists(String email){
        System.out.println("estest");
        testService1.test1();
        return false;
    }

    public String signUp(SignUpDTO signUpDTO){
        return "test";
    }
}
