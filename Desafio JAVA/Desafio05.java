package Aula01;

import java.util.Scanner;

public class Desafio05 {
    
        public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        System.out.println("Digite a letra: "); 
        char resp = entrada.next().charAt(0);

        if (resp == 'F'){
            System.out.println("Feminino"); 
        } else if (resp == 'M'){
            System.out.println("Masculino"); 
        } else {
            System.out.println("Letra Invalida!"); 
        }
    }

}