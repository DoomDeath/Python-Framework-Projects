package cl.pruebatecnica.dto;

import lombok.Data;

import java.time.LocalDateTime;
import java.util.List;
@Data
public class UserDTO {

    private Long id;
    private String name;
    private String email;
    private String password;
    private LocalDateTime created;
    private LocalDateTime modified;
    private String token;
    private List<PhoneDTO> phones;

}
