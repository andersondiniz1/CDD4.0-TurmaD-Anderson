package Aula01;

import java.util.Scanner;

public class Desafio01 {
    
        public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite 1º número: "); 
        double resp = entrada.nextDouble();

        Scanner entrada2 = new Scanner(System.in);
        System.out.println("Digite 2º número: "); 
        double resp2 = entrada2.nextDouble();

        Scanner entrada3 = new Scanner(System.in);
        System.out.println("Digite 3º número: "); 
        double resp3 = entrada3.nextDouble();

        if(resp > resp2 && resp > resp3){
            System.out.println("1º Numero é maior: "+resp); 
        } else if (resp2 > resp3){
            System.out.println("2º Numero é maior: "+resp2); 
        } else {
            System.out.println("3º Numero é maior: "+resp3);  
        }

        if(resp < resp2 && resp < resp3){
            System.out.println("1º Numero é menor: "+resp); 
        } else if (resp2 < resp3){
            System.out.println("2º Numero é menor: "+resp2); 
        } else {
            System.out.println("3º Numero é menor: "+resp3);  
        }
    }

}
