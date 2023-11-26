package Aula01;

import java.util.Scanner;

public class Desafio06 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int count = 0;

        System.out.println("Telefonou para a vítima? Digite 1 para sim, 2 para não: "); 
        int resp1 = entrada.nextInt();
        if(resp1 == 1){
            count++;
        }

        System.out.println("Esteve no local do crime? Digite 1 para sim, 2 para não: "); 
        int resp2 = entrada.nextInt();
        if(resp2 == 1){
            count++;
        }

        System.out.println("Mora perto da vítima? Digite 1 para sim, 2 para não: "); 
        int resp3 = entrada.nextInt();
        if(resp3 == 1){
            count++;
        }
            
        System.out.println("Devia para a vítima? Digite 1 para sim, 2 para não: "); 
        int resp4 = entrada.nextInt();
        if(resp4 == 1){
            count++;
        }

        System.out.println("Já trabalhou com a vítima? /n Digite 1 para sim, 2 para não: "); 
        int resp5 = entrada.nextInt();
        if(resp5 == 1){
            count++;
        }     

        if (count == 5){
            System.out.println("Assassino"); 
        } else if (count == 4 || count == 3){
            System.out.println("Cúmplice"); 
        } else if (count == 2){
            System.out.println("Suspeito"); 
        } else {
            System.out.println("Inocente"); 
        }
    }
}
