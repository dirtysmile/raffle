package com.raffleWeb.repository;

import com.raffleWeb.dto.entity.Member;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MemberRepository extends JpaRepository<Member, Long> {

}
