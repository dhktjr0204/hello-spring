package hello.servlet.domain.member;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.*;

public class MemberRepositoryTest {

    MemberRepository memberRepository=MemberRepository.getInstance();

    @AfterEach
    void afterEach(){
        memberRepository.clearStore();
    }//테스트 할 때마다 초기화

    @Test
    void save(){
        //given
        Member member=new Member("hello",20);

        //when
        Member savedMember = memberRepository.save(member);

        //then
        Member findMember = memberRepository.findById(savedMember.getId());
        assertThat(findMember).isEqualTo(savedMember);
    }

    @Test
    void findAll(){
        Member member1=new Member("Member1",20);
        Member member2=new Member("Member2",30);

        memberRepository.save(member1);
        memberRepository.save(member2);


        List<Member> result=memberRepository.findALl();

        assertThat(result.size()).isEqualTo(2);
        assertThat(result).contains(member1,member2);
    }
}
