package com.systemjaade.edad.util;

import java.time.LocalDate;
import java.time.Period;
import java.util.Date;

 
public class MetodoGenericos {

  public static String edad(Date fecha_nacimiento) {
    LocalDate fecha_nacimientoLD = DateUtils.asLocalDate(fecha_nacimiento);
    LocalDate hoy = LocalDate.now();
    Period periodo = Period.between(fecha_nacimientoLD, hoy);
    String an = (periodo.getYears() == 1) ? "año" : "años";
    String me = (periodo.getMonths() == 1) ? "mes" : "meses";
    String di = (periodo.getDays() == 1) ? "día" : "días";
    return periodo.getYears() + " " + an; // + ", y " + periodo.getMonths() + " " + me + ", y " + periodo.getDays() + " " + di;
  }
}
