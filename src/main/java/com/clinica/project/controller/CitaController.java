package com.clinica.project.controller;

import com.clinica.project.domain.service.CitaService;
import com.clinica.project.domain.dto.CitaCreateRequest;
import com.clinica.project.infrastructure.model.Doctor;
import com.clinica.project.infrastructure.model.Paciente;
import com.clinica.project.infrastructure.repository.DoctorRepository;
import com.clinica.project.infrastructure.repository.PacienteRepository;
import java.time.LocalDateTime;
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
    @Autowired private DoctorRepository doctorRepository;
    @Autowired private PacienteRepository pacienteRepository;

    @GetMapping
    @PreAuthorize("hasRole('DOCTOR') or hasRole('ADMIN')")
    public List<Cita> getAllCitas() {
        return citaService.findAll();
    }

    @PostMapping
    @PreAuthorize("hasRole('DOCTOR') or hasRole('ADMIN')")
    public Cita create(@RequestBody CitaCreateRequest req) {
        Doctor doctor = doctorRepository.findById(req.getDoctorId())
                .orElseThrow(() -> new org.springframework.web.server.ResponseStatusException(
                        org.springframework.http.HttpStatus.BAD_REQUEST, "Doctor no encontrado"));
        Paciente paciente = pacienteRepository.findById(req.getPacienteId())
                .orElseThrow(() -> new org.springframework.web.server.ResponseStatusException(
                        org.springframework.http.HttpStatus.BAD_REQUEST, "Paciente no encontrado"));

        LocalDateTime fecha;
        try {
            fecha = LocalDateTime.parse(req.getFechaHora());
        } catch (Exception e) {
            throw new org.springframework.web.server.ResponseStatusException(
                    org.springframework.http.HttpStatus.BAD_REQUEST, "Fecha y hora inválidas");
        }

        Cita c = new Cita();
        c.setDoctor(doctor);
        c.setPaciente(paciente);
        c.setMotivo(req.getMotivo());
        c.setFechaHora(fecha);
        return citaService.save(c);
    }
}
