package com.clinica.project.domain.dto;

import lombok.Data;

@Data
public class PacienteDTO {
    private Long id;
    private String nombre;
    private String apellido;
    private String dni;
}
