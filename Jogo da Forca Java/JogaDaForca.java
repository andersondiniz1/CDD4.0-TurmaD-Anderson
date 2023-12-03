import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String verificador = "s";

        while (verificador.equalsIgnoreCase("s")) {
            System.out.println("\n\n=== JOGO DA FORCA ===\n"
                    + "1  - Jogar \n"
                    + "=====================\n"
                    + "0 - Encerrar Jogo\n"
                    + "=====================\n");
            
            System.out.print("Escolha uma opção: ");
            String ops = scanner.nextLine();

            while (!ops.equals("1") && !ops.equals("0")) {
                System.out.print("Opção inválida, tente novamente...\n"
                        + "Escolha uma opção acima: ");
                ops = scanner.nextLine();
            }

            if (ops.equals("1")) {
                JogoDaForca();
            } else if (ops.equals("0")) {
                verificador = "0";
                System.out.println("\nFinalizando o Jogo...");
            } else {
                System.out.println("\nOpção inválida, tente novamente...\n");
            }
        }
    }

    // Implemente o método JogoDaForca() conforme necessário.
    private static void JogoDaForca() {
        // Implemente o corpo do jogo aqui.
        System.out.println("Jogo da Forca iniciado!");
    }
}
