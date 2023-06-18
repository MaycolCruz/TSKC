package GUI;

import ClasesPecados.Cliente;
import java.io.*;
import java.util.ArrayList;
import javax.swing.*;
import ClasesPecados.Venta;
import ClasesPecados.Habitacion;
import java.util.Date;
import java.util.concurrent.TimeUnit;
import javax.swing.JComboBox;
import javax.swing.JOptionPane;
import javax.swing.DefaultComboBoxModel;

public class AlquilerHabitaciones extends javax.swing.JFrame {
    
    Cliente nuevoCliente= new Cliente();//para leer el nuevo cliente desde el form
    Venta nuevaVenta=new Venta();//para configurar la venta actual
    ArrayList<Venta> ventas = new ArrayList<Venta>(); //para cargar las ventas del archivo
    ArrayList<Habitacion> habitaciones= new ArrayList<Habitacion>();// para recuperar las habitaciones
    
    
    public AlquilerHabitaciones() {
        initComponents();
        JComboBox<String> comboBox = jComboBox1;       
        cargarArchivoHabitaciones();
        configurarComboBox(comboBox);  
        obtenerDatosHabitacion();
        cargarArchivoVentas();             
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jPanel2 = new javax.swing.JPanel();
        GuardarAH = new javax.swing.JButton();
        CancelarAH = new javax.swing.JButton();
        jLabel13 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel12 = new javax.swing.JLabel();
        jLabel1 = new javax.swing.JLabel();
        jLabel8 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jLabel15 = new javax.swing.JLabel();
        jLabel11 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        jComboBox1 = new javax.swing.JComboBox<>();
        tipoHab = new javax.swing.JTextField();
        precioHab = new javax.swing.JTextField();
        nomC = new javax.swing.JTextField();
        apC = new javax.swing.JTextField();
        dniC = new javax.swing.JTextField();
        telefC = new javax.swing.JTextField();
        corrC = new javax.swing.JTextField();
        direC = new javax.swing.JTextField();
        jPanel3 = new javax.swing.JPanel();
        jLabel7 = new javax.swing.JLabel();
        fechaIngreso = new com.toedter.calendar.JDateChooser();
        fechaSalida = new com.toedter.calendar.JDateChooser();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);
        setTitle("Ventana Alquiler Habitación");

        jPanel1.setBackground(new java.awt.Color(35, 61, 78));

        jPanel2.setBackground(new java.awt.Color(255, 255, 255));

        GuardarAH.setBackground(new java.awt.Color(0, 51, 51));
        GuardarAH.setFont(new java.awt.Font("Dubai Light", 0, 14)); // NOI18N
        GuardarAH.setForeground(new java.awt.Color(255, 255, 255));
        GuardarAH.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Imagenes/SAVE.png"))); // NOI18N
        GuardarAH.setText("GUARDAR");
        GuardarAH.setBorder(javax.swing.BorderFactory.createEmptyBorder(1, 1, 1, 1));
        GuardarAH.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                GuardarAHActionPerformed(evt);
            }
        });

        CancelarAH.setBackground(new java.awt.Color(35, 61, 78));
        CancelarAH.setFont(new java.awt.Font("Dubai Light", 0, 14)); // NOI18N
        CancelarAH.setForeground(new java.awt.Color(255, 255, 255));
        CancelarAH.setIcon(new javax.swing.ImageIcon(getClass().getResource("/Imagenes/CANCELAR.png"))); // NOI18N
        CancelarAH.setText("CANCELAR");
        CancelarAH.setBorder(javax.swing.BorderFactory.createEmptyBorder(1, 1, 1, 1));
        CancelarAH.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                CancelarAHActionPerformed(evt);
            }
        });

        jLabel13.setBackground(new java.awt.Color(0, 51, 51));
        jLabel13.setFont(new java.awt.Font("Segoe UI", 0, 15)); // NOI18N
        jLabel13.setForeground(new java.awt.Color(51, 51, 51));
        jLabel13.setText("Dirección:");

        jLabel4.setBackground(new java.awt.Color(0, 51, 51));
        jLabel4.setFont(new java.awt.Font("Segoe UI", 0, 15)); // NOI18N
        jLabel4.setForeground(new java.awt.Color(0, 51, 51));
        jLabel4.setText("Correo electrónico:");

        jLabel3.setBackground(new java.awt.Color(0, 51, 51));
        jLabel3.setFont(new java.awt.Font("Segoe UI", 0, 15)); // NOI18N
        jLabel3.setForeground(new java.awt.Color(51, 51, 51));
        jLabel3.setText("Telefono/Celular:");

        jLabel2.setBackground(new java.awt.Color(0, 51, 51));
        jLabel2.setFont(new java.awt.Font("Segoe UI", 0, 15)); // NOI18N
        jLabel2.setForeground(new java.awt.Color(51, 51, 51));
        jLabel2.setText("DNI del cliente:");

        jLabel12.setBackground(new java.awt.Color(0, 51, 51));
        jLabel12.setFont(new java.awt.Font("Segoe UI", 0, 15)); // NOI18N
        jLabel12.setForeground(new java.awt.Color(51, 51, 51));
        jLabel12.setText("Apellido del cliente:");

        jLabel1.setBackground(new java.awt.Color(0, 51, 51));
        jLabel1.setFont(new java.awt.Font("Segoe UI", 0, 15)); // NOI18N
        jLabel1.setForeground(new java.awt.Color(51, 51, 51));
        jLabel1.setText("Nombre del cliente:");

        jLabel8.setFont(new java.awt.Font("Segoe UI", 0, 15)); // NOI18N
        jLabel8.setForeground(new java.awt.Color(0, 51, 51));
        jLabel8.setText("Fecha de salida:");

        jLabel6.setFont(new java.awt.Font("Segoe UI", 0, 15)); // NOI18N
        jLabel6.setForeground(new java.awt.Color(0, 51, 51));
        jLabel6.setText("Fecha de entrada:");

        jLabel15.setFont(new java.awt.Font("Segoe UI", 0, 15)); // NOI18N
        jLabel15.setForeground(new java.awt.Color(0, 51, 51));
        jLabel15.setText("Precio (s/.):");

        jLabel11.setFont(new java.awt.Font("Segoe UI", 0, 15)); // NOI18N
        jLabel11.setForeground(new java.awt.Color(0, 51, 51));
        jLabel11.setText("Tipo:");

        jLabel5.setFont(new java.awt.Font("Segoe UI", 0, 15)); // NOI18N
        jLabel5.setForeground(new java.awt.Color(0, 51, 51));
        jLabel5.setText("Habitación (número):");

        jLabel10.setBackground(new java.awt.Color(35, 61, 78));
        jLabel10.setFont(new java.awt.Font("Dubai Light", 1, 34)); // NOI18N
        jLabel10.setForeground(new java.awt.Color(35, 61, 78));
        jLabel10.setText("ALQUILAR HABITACIÓN");

        jComboBox1.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Item 1", "Item 2", "Item 3", "Item 4" }));
        jComboBox1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jComboBox1ActionPerformed(evt);
            }
        });

        tipoHab.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                tipoHabActionPerformed(evt);
            }
        });

        jPanel3.setBackground(new java.awt.Color(35, 61, 78));

        jLabel7.setFont(new java.awt.Font("Dubai", 0, 18)); // NOI18N
        jLabel7.setForeground(new java.awt.Color(255, 255, 255));
        jLabel7.setText("Complete los siguientes datos:");

        javax.swing.GroupLayout jPanel3Layout = new javax.swing.GroupLayout(jPanel3);
        jPanel3.setLayout(jPanel3Layout);
        jPanel3Layout.setHorizontalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jLabel7, javax.swing.GroupLayout.DEFAULT_SIZE, 301, Short.MAX_VALUE)
        );
        jPanel3Layout.setVerticalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jLabel7, javax.swing.GroupLayout.DEFAULT_SIZE, 36, Short.MAX_VALUE)
        );

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2.setLayout(jPanel2Layout);
        jPanel2Layout.setHorizontalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addComponent(jPanel3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup()
                .addGap(0, 0, Short.MAX_VALUE)
                .addComponent(jLabel10)
                .addGap(129, 129, 129))
            .addGroup(jPanel2Layout.createSequentialGroup()
                .addGap(147, 147, 147)
                .addComponent(CancelarAH, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(28, 28, 28)
                .addComponent(GuardarAH, javax.swing.GroupLayout.PREFERRED_SIZE, 126, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(0, 0, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup()
                .addContainerGap(67, Short.MAX_VALUE)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addComponent(jLabel13)
                        .addGap(76, 76, 76)
                        .addComponent(direC, javax.swing.GroupLayout.PREFERRED_SIZE, 300, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(jLabel15)
                            .addComponent(jLabel11))
                        .addGap(76, 76, 76)
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(tipoHab, javax.swing.GroupLayout.PREFERRED_SIZE, 300, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(precioHab, javax.swing.GroupLayout.PREFERRED_SIZE, 300, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addComponent(jLabel5)
                        .addGap(76, 76, 76)
                        .addComponent(jComboBox1, javax.swing.GroupLayout.PREFERRED_SIZE, 300, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(jLabel8)
                            .addComponent(jLabel6))
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel2Layout.createSequentialGroup()
                                .addGap(115, 115, 115)
                                .addComponent(fechaIngreso, javax.swing.GroupLayout.PREFERRED_SIZE, 206, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(55, 55, 55))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup()
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(fechaSalida, javax.swing.GroupLayout.PREFERRED_SIZE, 206, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addGap(65, 65, 65))))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addComponent(jLabel1)
                        .addGap(76, 76, 76)
                        .addComponent(nomC, javax.swing.GroupLayout.PREFERRED_SIZE, 300, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addComponent(jLabel12)
                        .addGap(76, 76, 76)
                        .addComponent(apC, javax.swing.GroupLayout.PREFERRED_SIZE, 300, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addComponent(jLabel2)
                        .addGap(76, 76, 76)
                        .addComponent(dniC, javax.swing.GroupLayout.PREFERRED_SIZE, 300, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addComponent(jLabel3)
                        .addGap(76, 76, 76)
                        .addComponent(telefC, javax.swing.GroupLayout.PREFERRED_SIZE, 300, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addComponent(jLabel4)
                        .addGap(76, 76, 76)
                        .addComponent(corrC, javax.swing.GroupLayout.PREFERRED_SIZE, 300, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(62, 62, 62))
        );
        jPanel2Layout.setVerticalGroup(
            jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel2Layout.createSequentialGroup()
                .addGap(21, 21, 21)
                .addComponent(jLabel10)
                .addGap(12, 12, 12)
                .addComponent(jPanel3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(jPanel2Layout.createSequentialGroup()
                                .addGap(27, 27, 27)
                                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(jComboBox1, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(jLabel5, javax.swing.GroupLayout.PREFERRED_SIZE, 36, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(jLabel11, javax.swing.GroupLayout.PREFERRED_SIZE, 36, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(tipoHab, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addGap(18, 18, 18)
                                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                                    .addComponent(jLabel15, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                    .addComponent(precioHab, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                                .addComponent(jLabel6, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addGroup(jPanel2Layout.createSequentialGroup()
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addComponent(fechaIngreso, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jLabel8, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel2Layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(fechaSalida, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(18, 18, 18)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(nomC, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(apC, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel12, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel2, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(dniC, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(telefC, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(corrC, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel4, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(direC, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel13, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(66, 66, 66)
                .addGroup(jPanel2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(GuardarAH, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(CancelarAH, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(122, 122, 122))
        );

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jPanel2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jPanel2, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addContainerGap())
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel1, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void GuardarAHActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_GuardarAHActionPerformed
        cargarArchivoVentas();
        obtenerClienteyFechas();     
    }//GEN-LAST:event_GuardarAHActionPerformed

    private void CancelarAHActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_CancelarAHActionPerformed
        // TODO add your handling code here:
        this.setVisible(false);
    }//GEN-LAST:event_CancelarAHActionPerformed

//
    private void jComboBox1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jComboBox1ActionPerformed
        // cuando hay un evento
        obtenerDatosHabitacion();
    }//GEN-LAST:event_jComboBox1ActionPerformed

    private void tipoHabActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_tipoHabActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_tipoHabActionPerformed
    
     private void cargarArchivoHabitaciones(){
        habitaciones.clear();
        //leyendo las habitaciones que ya se habian cargado en el sistema          
        try{
            //para leer archivos desde un .dat
            FileInputStream archivo = new FileInputStream("habitaciones.dat");// aqui abre el archivo
            ObjectInputStream objetoEntrada = new ObjectInputStream(archivo);// aqui recuper los objetos guardados en el archivo           
            boolean finDeArchivo=false;
            while(!finDeArchivo){
                try{
                    habitaciones.add((Habitacion)objetoEntrada.readObject());
                }
                catch(EOFException e){
                    finDeArchivo=true;
                }
                catch(Exception f){
                       finDeArchivo=true;
//                    JOptionPane.showMessageDialog(null, "error 1");
                }
            }
            objetoEntrada.close();
        }
        catch(IOException e){
//            JOptionPane.showMessageDialog(null, "error 2");
        }
    }
    
    ArrayList<Integer> leerNumerosHabitaciones() {
    ArrayList<Integer> numerosHabitaciones = new ArrayList<Integer>();   
    for(int i=0;i<habitaciones.size();i++){
        
        numerosHabitaciones.add(habitaciones.get(i).getNumero());
    }
    return numerosHabitaciones;
    } 
   
    private void configurarComboBox(JComboBox comboBox) {
    ArrayList<Integer> numerosHabitaciones = leerNumerosHabitaciones();
    DefaultComboBoxModel<Integer> model = new DefaultComboBoxModel<Integer>(numerosHabitaciones.toArray(new Integer[numerosHabitaciones.size()]));
    comboBox.setModel(model);
    } 
     
     void obtenerDatosHabitacion(){//para mostrrrayList<Integer> numerosHabitaciones = leerNumerosHabitaciones();ar los campos tipo de habitación y fecha
     int numSelec =(int)jComboBox1.getSelectedItem();//obteniendo el numero de habitación seleccionado
     int indice=0; //inicializando un indice  
     for(int i=0;i<habitaciones.size();i++){
         if(habitaciones.get(i).getNumero()==numSelec){
             indice=i;
         }
     }
     tipoHab.setText(habitaciones.get(indice).getTipo());
     precioHab.setText(Double.toString(habitaciones.get(indice).getPrecioxDia()));    
     nuevaVenta.setHabitacion(habitaciones.get(indice));//aqui guarda la habitación en el nuevaVenta
    } 
     
    private void obtenerClienteyFechas(){
        //la función obtiene los datos para la venta y las guarda en el array de ventas
        if(nomC.getText().isEmpty()||apC.getText().isEmpty()||corrC.getText().isEmpty()||dniC.getText().isEmpty()||direC.getText().isEmpty()||telefC.getText().isEmpty()){   
            JOptionPane.showMessageDialog(null,"Los datos del cliente no estan completos");
        }
        else{
            nuevoCliente.setNombres(nomC.getText());
            nuevoCliente.setApellidos(apC.getText());
            nuevoCliente.setCorreo(corrC.getText());
            nuevoCliente.setDni(dniC.getText());
            nuevoCliente.setDireccion(direC.getText());
            nuevoCliente.setTelefono(telefC.getText());           
            nuevaVenta.setCliente(nuevoCliente);//guardando el cliente en la venta       
            // obteniendo fechas       
        long dif=fechaSalida.getDate().getTime()-fechaIngreso.getDate().getTime();
        TimeUnit time = TimeUnit.DAYS;
        int dias = (int)time.convert(dif, TimeUnit.MILLISECONDS);           
        if(fechaSalida.getDate()==null||fechaSalida.getDate()==null||dias<=0){       
            JOptionPane.showMessageDialog(null,"Las fechas no son correctas");      
        }
        else{
            nuevaVenta.setFechaIngreso(fechaIngreso.getDate());//guarda la fecha de ingreso en la venta nueva
            nuevaVenta.setFechaSalida(fechaSalida.getDate());//guarda la fecha de salida en la venta nueva
            nuevaVenta.setDias(dias);           
            Date fechaActual = new Date(); //obteniendo fecha actual
            nuevaVenta.setFechaVenta(fechaActual);//
            ventas.add(nuevaVenta);//aqui guarda la nueva ventas en el array de ventas
            guardarArchivoVentas();//aqui guarda el archivo .dat
            calcularPrecio();         
        }    
        }      
    }
    
    void calcularPrecio(){
        double precio=0;
        precio=nuevaVenta.getDias()*nuevaVenta.getHabitacion().getPrecioxDia();
        JOptionPane.showMessageDialog(null, "Venta Completa!, total: s/. "+precio);
    }
  
    void limpiarDatos(){
    fechaIngreso.setDate(null);
    fechaSalida.setDate(null);
    nomC.setText("");
    apC.setText("");
    dniC.setText("");
    telefC.setText("");
    corrC.setText("");
    direC.setText("");
    }
 
    private void guardarArchivoVentas(){
        try{
            //para guardar empleados en el dat
            FileOutputStream archivo = new FileOutputStream("ventas.dat");//vincula el archivo                                
            ObjectOutputStream objetoSalida = new ObjectOutputStream(archivo);// captura el objeto a guardar          
            for(int i=0;i<ventas.size();i++){
                objetoSalida.writeObject(ventas.get(i));//escribe uno a uno los objetos guardados en el array             
            }
            objetoSalida.close();
            limpiarDatos();          
        }
        catch(IOException e){
            JOptionPane.showMessageDialog(null, e.getMessage());
        }                       
    }
     
    private void cargarArchivoVentas(){
        ventas.clear();
        //leyendo las ventas que ya se habian cargado en el sistema                
        try{
            //para leer archivos desde un .dat
            FileInputStream archivo = new FileInputStream("ventas.dat");// aqui abre el archivo
            ObjectInputStream objetoEntrada = new ObjectInputStream(archivo);// aqui recuper los objetos guardados en el archivo         
            boolean finDeArchivo=false;
            while(!finDeArchivo){
                try{
                    ventas.add((Venta)objetoEntrada.readObject());
                }
                catch(EOFException e){
                    finDeArchivo=true;
                }
                catch(Exception f){
                       finDeArchivo=true;

//                    JOptionPane.showMessageDialog(null, "error 1");
                }
            }
            objetoEntrada.close();
        }
        catch(IOException e){
//            JOptionPane.showMessageDialog(null, "error 2");
        }
//        for(int i=0; i<ventas.size();i++){
//            System.out.println(ventas.get(i).toString());
//        }     
    }
    
        void mostrarArchivoVentas(){
        cargarArchivoVentas();
        for(int i=0; i<ventas.size();i++){
            System.out.println(ventas.get(i).toString());
        }     
        }        
    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(AlquilerHabitaciones.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(AlquilerHabitaciones.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(AlquilerHabitaciones.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(AlquilerHabitaciones.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new AlquilerHabitaciones().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton CancelarAH;
    private javax.swing.JButton GuardarAH;
    private javax.swing.JTextField apC;
    private javax.swing.JTextField corrC;
    private javax.swing.JTextField direC;
    private javax.swing.JTextField dniC;
    private com.toedter.calendar.JDateChooser fechaIngreso;
    private com.toedter.calendar.JDateChooser fechaSalida;
    private javax.swing.JComboBox<String> jComboBox1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel11;
    private javax.swing.JLabel jLabel12;
    private javax.swing.JLabel jLabel13;
    private javax.swing.JLabel jLabel15;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JTextField nomC;
    private javax.swing.JTextField precioHab;
    private javax.swing.JTextField telefC;
    private javax.swing.JTextField tipoHab;
    // End of variables declaration//GEN-END:variables
}
