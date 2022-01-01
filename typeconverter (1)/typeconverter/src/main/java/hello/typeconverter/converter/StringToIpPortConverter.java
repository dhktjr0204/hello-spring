package hello.typeconverter.converter;

import hello.typeconverter.type.IpPort;
import org.springframework.core.convert.converter.Converter;

public class StringToIpPortConverter implements Converter<String , IpPort> {
    @Override
    public IpPort convert(String source) {
        String[] split = source.split(":");
        String ip=split[0];
        int port=Integer.parseInt(split[1]);
        return new IpPort(ip,port);
    }
}
