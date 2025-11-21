package com.clinica.project.domain.dto;

public class CitaCreateRequest {
    private Long doctorId;
    private Long pacienteId;
    private String fechaHora; // ISO-8601 "yyyy-MM-ddTHH:mm"
    private String motivo;

    public Long getDoctorId() { return doctorId; }
    public void setDoctorId(Long doctorId) { this.doctorId = doctorId; }
    public Long getPacienteId() { return pacienteId; }
    public void setPacienteId(Long pacienteId) { this.pacienteId = pacienteId; }
    public String getFechaHora() { return fechaHora; }
    public void setFechaHora(String fechaHora) { this.fechaHora = fechaHora; }
    public String getMotivo() { return motivo; }
    public void setMotivo(String motivo) { this.motivo = motivo; }
}
