package cl.pruebatecnica.dto;

import cl.pruebatecnica.entity.Phone;
import cl.pruebatecnica.entity.User;
import lombok.Data;
import org.modelmapper.ModelMapper;

import java.util.List;
import java.util.stream.Collectors;

@Data
public class UserRequest {

    private String name;
    private String email;
    private String password;
    private List<PhoneRequest> phones;
    private List<String> deletedPhones;
    private List<String> addedPhones;

}
