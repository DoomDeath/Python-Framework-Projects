package cl.pruebatecnica.dto;

import lombok.Data;

import java.time.LocalDateTime;
import java.util.List;

@Data
public class RegisterResponse {

    Long id;
    LocalDateTime created;
    LocalDateTime modified;
    String token;

    public RegisterResponse(Long id, LocalDateTime created, LocalDateTime modified, String token, String name, String email, List<String> phoneNumbers) {
    }

    public RegisterResponse() {

    }
}
