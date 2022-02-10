package com.raffleWeb.dto.entity;

import lombok.AccessLevel;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Entity
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class SiteItem {

    @Id @GeneratedValue
    @Column(name = "SITE_ITME_ID")
    private Long id;
    private String name;
    private String url;

    @ManyToOne
    @JoinColumn(name = "SITE_ID")
    private Site site;

    public SiteItem(String name, String url) {
        this.name = name;
        this.url = url;
    }
}
