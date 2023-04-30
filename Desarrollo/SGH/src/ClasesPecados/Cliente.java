package ClasesPecados;

import java.io.*;


public class Cliente implements Serializable{
    private String nombres;
    private String apellidos;
    private String dni;
    private String correo;
    private String telefono;
    private String direccion;
    
    public Cliente() {      
    }
    
    public Cliente(String nombre, String apellido) {
        this.nombres = nombre;
        this.apellidos = apellido;
    }

    public String getNombres() {
        return nombres;
    }

    public void setNombres(String nombres) {
        this.nombres = nombres;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    @Override
    public String toString() {
        return "Cliente{" + "nombres=" + nombres + ", apellidos=" + apellidos + ", dni=" + dni + ", correo=" + correo + ", telefono=" + telefono + ", direccion=" + direccion + '}';
    }

    
  
    
}