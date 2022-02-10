package com.raffleWeb.controller;

import com.raffleWeb.service.ExecuteShellService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.concurrent.ExecutorService;

@RestController
@RequestMapping("execute")
@RequiredArgsConstructor
public class ExecController {

    private final ExecuteShellService executeShellService;

    @PostMapping("/")
    public void test(@RequestBody HashMap p){
        System.out.println(p.get("cmd"));
        executeShellService.excute((String)p.get("cmd"));
    }

    @PostMapping("/test")
    public HashMap test3(@RequestBody HashMap p){
        System.out.println(p);
        return p;
    }

    @GetMapping("/")
    public void test2(){
        System.out.println("test");
        System.out.println("test");
        System.out.println("test");
        System.out.println("test");
        System.out.println("test");
        System.out.println("test");
        System.out.println("test");
    }
}
