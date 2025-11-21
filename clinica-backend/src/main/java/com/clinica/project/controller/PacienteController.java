package com.clinica.project.controller;

import com.clinica.project.domain.service.PacienteService;
import com.clinica.project.infrastructure.model.Paciente;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/pacientes")
public class PacienteController {
    @Autowired
    private PacienteService pacienteService;

    @GetMapping
    @PreAuthorize("hasRole('USER') or hasRole('DOCTOR') or hasRole('ADMIN')")
    public List<Paciente> getAllPacientes() {
        return pacienteService.findAll();
    }

    @PostMapping
    @PreAuthorize("hasRole('DOCTOR') or hasRole('ADMIN')")
    public Paciente createPaciente(@RequestBody Paciente paciente) {
        return pacienteService.save(paciente);
    }
}
