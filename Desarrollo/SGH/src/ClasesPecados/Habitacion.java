package ClasesPecados;

import java.io.*;

public class Habitacion implements Serializable{
    
    private int numero;
    private boolean estado;
    private String tipo;
    private double precioxDia;
    
    public Habitacion() {
        
    }
    
    public Habitacion(int numero, String tipo, double precioxDia) {
        this.numero = numero;
        this.tipo = tipo;
        this.precioxDia = precioxDia;
        this.estado=false;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public boolean isEstado() {
        return estado;
    }

    public void setEstado(boolean estado) {
        this.estado = estado;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public double getPrecioxDia() {
        return precioxDia;
    }

    public void setPrecioxDia(double precioxDia) {
        this.precioxDia = precioxDia;
    }

    @Override
    public String toString() {
        return "Habitacion{" + "numero=" + numero + ", estado=" + estado + ", tipo=" + tipo + ", precioxDia=" + precioxDia + '}';
    }   
}
