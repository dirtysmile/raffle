package com.raffleWeb.dto.entity;

import lombok.AccessLevel;
import lombok.NoArgsConstructor;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Site {
    @Id @GeneratedValue
    @Column(name = "SITE_ID")
    private Long id;
    private String name;
    private String url;

    public Site(String name) {
        this.name = name;
    }

    public Site(String name, String url) {
        this.name = name;
        this.url = url;
    }
}
