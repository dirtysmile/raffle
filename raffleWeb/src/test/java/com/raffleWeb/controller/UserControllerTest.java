package com.raffleWeb.controller;

import com.google.gson.Gson;
import com.raffleWeb.dto.SignUpDTO;
import com.raffleWeb.dto.User;
import com.raffleWeb.service.UserService;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.ArgumentMatchers;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;
import org.mockito.junit.jupiter.MockitoSettings;
import org.mockito.quality.Strictness;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MockMvcBuilder;
import org.springframework.test.web.servlet.MvcResult;
import org.springframework.test.web.servlet.ResultActions;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import static org.junit.jupiter.api.Assertions.*;
@ExtendWith(MockitoExtension.class)
@MockitoSettings(strictness = Strictness.LENIENT)
class UserControllerTest {

    @InjectMocks
    private UserController userController;

    @Mock
    private UserService userService;

    private MockMvc mockMvc;

    @BeforeEach
    public void init(){
        mockMvc = MockMvcBuilders.standaloneSetup(userController).build();
    }

    @DisplayName("회원 가입 성공")
    @Test
    void signUpSuccess() throws Exception {
        //given
        final SignUpDTO signUpDTO = signUpDTO();
        Mockito.doReturn(false).when(userService).isEmailExists(signUpDTO.getEmail());
        Mockito.doReturn("String").when(userService).signUp(ArgumentMatchers.any(SignUpDTO.class));

        //when
        final ResultActions resultActions = mockMvc.perform(
                MockMvcRequestBuilders.post("/user/signUp")
                .contentType(MediaType.APPLICATION_JSON)
                .content(new Gson().toJson(signUpDTO))
        );

        //then
        final MvcResult mvcResult = resultActions.andExpect(MockMvcResultMatchers.status().isOk()).andReturn();
        final String token = mvcResult.getResponse().getContentAsString();
        org.assertj.core.api.Assertions.assertThat(token).isNotNull();
    }

    private SignUpDTO signUpDTO(){
        final SignUpDTO signUpDTO = new SignUpDTO();
        signUpDTO.setEmail("toto");
        return signUpDTO;
    }
}