package com.raffleWeb.controller;

import com.raffleWeb.dto.SignUpDTO;
import com.raffleWeb.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.Errors;
import org.springframework.web.bind.annotation.*;

@RequiredArgsConstructor
@RestController
@RequestMapping("user")
public class UserController {

    private final UserService userService;

    @PostMapping("/signUp")
    public ResponseEntity<String> signUp(@RequestBody final SignUpDTO signUpDTO){
        return userService.isEmailExists(signUpDTO.getEmail())
                ? ResponseEntity.badRequest().body("test")
                : ResponseEntity.ok(userService.signUp(signUpDTO));
    }

//    @GetMapping(value = "/list")
//    public ResponseEntity<UserListResponseDTO> findAll() {
//        final UserListResponseDTO userListResponseDTO = UserListResponseDTO.builder()
//                .userList(userService.findAll()).build();
//
//        return ResponseEntity.ok(userListResponseDTO);
//    }

}
