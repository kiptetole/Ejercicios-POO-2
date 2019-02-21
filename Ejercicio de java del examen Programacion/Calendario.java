/**
 * Ejercicio de menu del tiempo del examen de programacion:
 * 
 *  Menu:
 *  ------------
 *  1.- Introducir fecha.
 *  2.- Sumar dias a la fecha guardada.(Fecha previamente guardada.)
 *  3.- Restar dias a la fecha guardada.(Fecha previamente guardada.)
 *  4.- Comprobar fecha con otra introducida.(Fecha previamente guardada.)
 *  5.- Mostrar fecha.(Fecha previamente guardada.)
 *  6.- Salir del Programa.
 */
package v.uno;
 
/**
 * @author Jose Notario Millan
 */

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Scanner;

public class Calendario {
  /**
   * Este es el metodo main.
   * 
   * @param args
   */
  public static void main(String[] args) {
    Scanner s = new Scanner(System.in);
    SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy"); // El formato con el que se mostrara la fecha.
    Calendar a = GregorianCalendar.getInstance();
    Calendar a2 = GregorianCalendar.getInstance();
    // Inicializamos las variables.
    int selector;                           // Variable entera que hace de selector del menu de eleccion.
    int diasSumRes;                         // Variable entera que suma o restat los dias a la fecha segum toque.
    String Fecha = "";
    
    do {
      menu();
      selector = s.nextInt();
      s.nextLine();
      
      switch (selector) {
      case 1:                 // Opcion de Introduccion de fecha.
        a = Verifica();
        Fecha = sdf.format(a.getTime());
        break;
      case 2:
        if (Fecha == "") {
          System.out.println("No hay Fecha");
        }else {
          // Suma dias a la fecha guardada
          System.out.println("Introduce los dias a sumar a la fecha:");
          diasSumRes = s.nextInt();
          a.add(Calendar.DATE, diasSumRes);
          System.out.println("La fecha es:" + sdf.format(a.getTime()));
        }
        break;
      case 3:
        if (Fecha == "") {
          System.out.println("No hay Fecha");
        }else {
            //Resta dias a la fecha guardada. 
            System.out.println("Introduce los dias a restar a la fecha:");
            diasSumRes = s.nextInt();
            a.add(Calendar.DATE, -diasSumRes);
            System.out.println("La fecha es:" + sdf.format(a.getTime()));
        }
        break;
      case 4:
        if (Fecha == "") {
          System.out.println("No hay Fecha");
        }else {
          System.out.println("Comparamos dos fechas: La guardada y la introducida.");
          a2 = Verifica();
          
          // Imprime por pantalla segun sea la fecha menor o mayor.
          if (a.compareTo(a2)>0){
              System.out.println("La fecha guardada es mayor que la introducida.");
          }else {
              System.out.println("La fecha guardada es menor que la introducida.");
          }
        }
        break;
      case 5:
        if (Fecha == "") {
          System.out.println("No hay Fecha");
        }else {
          System.out.println("La fecha guardada es:" + sdf.format(a.getTime()));
        }
        break;
      case 6:
        System.out.println("Adios :)");
        break;
      default:
        System.out.println("No existe esta opcion.");
        break;
      }
      
      
      
    }while(selector!=6);
    
  }
  
  /**
   * Muestra el menu del tiempo.
   */
  public static void menu() {
    System.out.println("Menu:\n----------------");
    System.out.println("1.- Añadir fecha al programa.");
    System.out.println("2.- Sumar dias a la fecha guardada.");
    System.out.println("3.- Restar dias a la fecha guardada.");
    System.out.println("4.- Comprobar fecha con otra introducida.");
    System.out.println("5.- Mostrar fecha.");
    System.out.println("6.- Salir.");
    System.out.println("Elegir opcion entre (1-6):");
  }
  
  /**
   * @param  String <Fecha que hemos introducdo anteriormente.>
   * @return  Calendar<Devuelve la fecha formateada>
   * 
   * Este formatea la fecha y la guarda en el objeto para su posterior uso. 
  */
  public static Calendar optenerFecha(String Fecha) {
    Calendar a = GregorianCalendar.getInstance();
    String[] parts;
    int d,m,y;
    
    if (Fecha.contains("/") && Fecha.length()==10) {
      parts = Fecha.split("/");
      d = Integer.parseInt(parts[0]);
      m = Integer.parseInt(parts[1]);
      y = Integer.parseInt(parts[2]);
      
      // Introducimos el por medio de un switch.
      // Por cada case introducimos los meses correspondientes.
      switch (m) {
      case 1:
        a.set(y, Calendar.JANUARY, d);
        break;
      case 2:
        a.set(y, Calendar.FEBRUARY, d);
        break;
      case 3:
        a.set(y, Calendar.MARCH, d);
        break;
      case 4:
        a.set(y, Calendar.APRIL, d);
        break;
      case 5:
        a.set(y, Calendar.MAY, d);
        break;
      case 6:
        a.set(y, Calendar.JUNE, d);
        break;
      case 7:
        a.set(y, Calendar.JULY, d);
        break;
      case 8:
        a.set(y, Calendar.AUGUST, d);
        break;
      case 9:
        a.set(y, Calendar.SEPTEMBER, d);
        break;
      case 10:
        a.set(y, Calendar.OCTOBER, d);
        break;
      case 11:
        a.set(y, Calendar.NOVEMBER, d);
        break;
      case 12:
        a.set(y, Calendar.DECEMBER, d);
        break;
      default:
          a.set(0, 0, 0);
        break;
      }
    }else {
      a.set(0, 0, 0);
    }
    return a;
  }
  
  /**
   * Esto verifica si la fecha introducida es correcta.
   * 
   * @return Calendar
   */
  public static Calendar Verifica() {
      Scanner s = new Scanner(System.in);
      SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
      Calendar a = GregorianCalendar.getInstance();
      String Fecha , Verifica;
      
      do {
          System.out.println("Introduzca la fecha: ");        // Se Introduce la fecha a guardar
          Fecha = s.nextLine();
          // Devuelve la fecha.
          a = optenerFecha(Fecha);
          // La introduce en una cadena, formateada.
          Verifica = sdf.format(a.getTime());
          
          if (!Fecha.equals(Verifica)) {
            System.out.println("Fecha mal introducida");
          }
          }while(!Fecha.equals(Verifica));
      // Se comparan las dos fechas para ver si son iguales.
      // Esto es para ver si la fecha se ha introducido bien.
      return a;
  }
}