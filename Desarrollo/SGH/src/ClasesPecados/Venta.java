package ClasesPecados;

import java.io.*;
import java.util.*;

public class Venta implements Serializable{
    private Cliente cliente;
    private Habitacion habitacion;
    private Date fechaIngreso;
    private Date fechaSalida;
    private Date fechaVenta;
    private int dias;

    public Venta() {
    }

    public Venta(Cliente cliente, Habitacion habitacion, Date fechaIngreso, Date fechaSalida, Date fechaVenta, int dias) {
        this.cliente = cliente;
        this.habitacion = habitacion;
        this.fechaIngreso = fechaIngreso;
        this.fechaSalida = fechaSalida;
        this.fechaVenta = fechaVenta;
        this.dias = dias;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public Habitacion getHabitacion() {
        return habitacion;
    }

    public void setHabitacion(Habitacion habitacion) {
        this.habitacion = habitacion;
    }

    public Date getFechaIngreso() {
        return fechaIngreso;
    }

    public void setFechaIngreso(Date fechaIngreso) {
        this.fechaIngreso = fechaIngreso;
    }

    public Date getFechaSalida() {
        return fechaSalida;
    }

    public void setFechaSalida(Date fechaSalida) {
        this.fechaSalida = fechaSalida;
    }

    public Date getFechaVenta() {
        return fechaVenta;
    }

    public void setFechaVenta(Date fechaVenta) {
        this.fechaVenta = fechaVenta;
    }

    public int getDias() {
        return dias;
    }

    public void setDias(int dias) {
        this.dias = dias;
    }

    @Override
    public String toString() {
        return "Venta{" + "cliente=" + cliente + ", habitacion=" + habitacion + ", fechaIngreso=" + fechaIngreso + ", fechaSalida=" + fechaSalida + ", fechaVenta=" + fechaVenta + ", dias=" + dias + '}';
    }

       
    
    
    
}
