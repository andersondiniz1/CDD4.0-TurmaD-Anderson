package Aula01;

import java.util.Scanner;

public class Desafio04 {
    
        public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Digite 1º nota: "); 
        double resp = entrada.nextDouble();

        System.out.println("Digite 2º nota: "); 
        double resp2 = entrada.nextDouble();
            
        double media = (resp + resp2) / 2;


        if (media >= 7 && media <= 10){
            System.out.println("Aprovado por média: "+media); 
        } else if (media <= 4 && media >= 0){
            System.out.println("Reprovado por média: "+media); 
        } else if (media >= 4 && media <= 7){
            System.out.println("Recuperação por média: "+media); 
        } else {
            System.out.println("Número invalido!"); 
        }
    }

}
