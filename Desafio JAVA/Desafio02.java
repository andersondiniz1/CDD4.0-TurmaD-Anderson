package Aula01;

import java.util.Scanner;

public class Desafio02 {
    
        public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite o número: "); 
        double resp = entrada.nextDouble();

        System.out.println(resp == 0 ? "Neutro" : resp > 0 ? "positivo" : "negativo"); // ? - IF simplificado | : - Else simplificado
    }

}
