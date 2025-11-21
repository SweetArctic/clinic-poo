package com.clinica.project.controller;

import com.clinica.project.domain.service.CitaService;
import com.clinica.project.infrastructure.model.Cita;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/citas")
public class CitaController {
    @Autowired
    private CitaService citaService;

    @GetMapping
    @PreAuthorize("hasRole('DOCTOR') or hasRole('ADMIN')")
    public List<Cita> getAllCitas() {
        return citaService.findAll();
    }
}