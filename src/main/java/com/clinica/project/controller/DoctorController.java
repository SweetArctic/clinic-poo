package com.clinica.project.controller;

import com.clinica.project.domain.service.DoctorService;
import com.clinica.project.infrastructure.model.Doctor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/doctores")
public class DoctorController {
    @Autowired
    private DoctorService doctorService;

    @GetMapping
    @PreAuthorize("hasRole('USER') or hasRole('DOCTOR') or hasRole('ADMIN')")
    public List<Doctor> getAllDoctores() {
        return doctorService.findAll();
    }
}