package cl.pruebatecnica.dto;

import lombok.Data;

@Data
public class ErrorResponse {

    Integer code;
    String message;
}
