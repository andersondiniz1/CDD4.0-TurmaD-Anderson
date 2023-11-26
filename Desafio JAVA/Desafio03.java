package Aula01;

import java.util.Scanner;

public class Desafio03 {
    
        public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite 1º número: "); 
        double resp = entrada.nextDouble();


        if (resp == 1){
            System.out.println(resp+": Domingo"); 
        } else if (resp == 2){
            System.out.println(resp+": Segunda"); 
        } else if (resp == 3){
            System.out.println(resp+": Terça"); 
        } else if (resp == 4){
            System.out.println(resp+": Quarta"); 
        } else if (resp == 5){
            System.out.println(resp+": Quinta"); 
        } else if (resp == 6){
            System.out.println(resp+": Sextas"); 
        } else if (resp == 7){
            System.out.println(resp+": Sabado"); 
        } else {
            System.out.println("Número invalido!"); 
        }
    }

}
