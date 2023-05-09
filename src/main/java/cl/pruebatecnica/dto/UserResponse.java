package cl.pruebatecnica.dto;

import lombok.Data;

import java.time.LocalDateTime;
import java.util.List;
@Data
public class UserResponse {
    private Long id;
    private String name;
    private String email;
    private LocalDateTime created;
    private LocalDateTime modified;
    private String token;
    private List<String> phones;

}
