package hello.springmvc.basic;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController//그냥 컨트롤러는 뷰로 반환
//레스트로하면 스트링자체로 반환
public class LogTestController {

    private final Logger log= LoggerFactory.getLogger(getClass());

    @RequestMapping("/log-test")
    public String logTest(){
        String name="Spring";

        log.trace("trace log={}",name);
        log.debug("debug log={}",name);
        log.info("info log={}",name);
        log.warn("warn log={}",name);
        log.error("error log={}",name);

        return "ok";
    }

}
