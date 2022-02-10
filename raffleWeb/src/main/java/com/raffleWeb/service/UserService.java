package com.raffleWeb.service;

import com.raffleWeb.dto.SignUpDTO;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserService {

    public boolean isEmailExists(String email){
        System.out.println("estest");
        return false;
    }

    public String signUp(SignUpDTO signUpDTO){
        return "test";
    }
}
