import java.util.Random;
import java.util.Scanner;

public class JogaDaForca {
    private String[][] palavras = {
            {"python", "Uma linguagem de programação"},
            {"cdd4.0", "Melhor curso"},
            {"ladrão", "Tem muito na cidade de Recife"},
            {"wellington", "Melhor professor"},
            {"casa", "Um lugar para relaxar"},
            {"janga", "Um lugar cheio de árvores e vida selvagem."},
            {"computador", "Um animal de estimação leal e amigável."},
            {"onibus", "Um meio de transporte com quatro rodas."}
    };

    private String palavra;
    private String dica;
    private StringBuilder letrasCertas = new StringBuilder();
    private StringBuilder letrasErradas = new StringBuilder();
    private int tentativas = 0;
    private int maxTentativas = 3;

    public void iniciarJogo() {
        escolherPalavra();
        System.out.println("=============================\n"
                + "Bem-vindo ao Jogo da Forca!\n"
                + "=============================\n");

        String palavraOculta = ocultarLetras();

        System.out.println("Dica: " + dica);
        System.out.println("Palavra: " + palavraOculta);

        while (true) {
            System.out.print("Digite uma letra: ");
            Scanner scanner = new Scanner(System.in);
            String letra = scanner.nextLine().toLowerCase();

            if (letrasCertas.indexOf(letra) != -1 || letrasErradas.indexOf(letra) != -1) {
                System.out.println("Você já tentou essa letra.");
                continue;
            }

            if (palavra.contains(letra)) {
                letrasCertas.append(letra);
                palavraOculta = ocultarLetras();
                System.out.println("Palavra: " + palavraOculta);

                if (palavraOculta.equals(palavra)) {
                    System.out.println("========================"
                            + "Parabéns! Você venceu."
                            + "========================");
                    break;
                }
            } else {
                letrasErradas.append(letra);
                tentativas++;
                exibirForca();

                if (tentativas == maxTentativas) {
                    System.out.println("\nFim de jogo! Você perdeu. A palavra era: " + palavra);
                    break;
                }
            }
        }
    }

    private void escolherPalavra() {
        Random random = new Random();
        int escolha = random.nextInt(palavras.length);
        palavra = palavras[escolha][0];
        dica = palavras[escolha][1];
    }

    private void exibirForca() {
        String[] partesForca = {"  O", " /|\\", " / \\"};
        System.out.println("\n=========== FORCA ===========");
        for (int i = 0; i < tentativas && i < partesForca.length; i++) {
            System.out.println(partesForca[i]);
        }
        System.out.println("=============================\n");
    }

    private String ocultarLetras() {
        StringBuilder resultado = new StringBuilder();
        for (char letra : palavra.toCharArray()) {
            if (letrasCertas.indexOf(String.valueOf(letra)) != -1) {
                resultado.append(letra);
            } else {
                resultado.append("_");
            }
        }
        return resultado.toString();
    }

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
                JogaDaForca jogo = new JogaDaForca();
                jogo.iniciarJogo();
            } else if (ops.equals("0")) {
                verificador = "0";
                System.out.println("\nFinalizando o Jogo...");
            } else {
                System.out.println("\nOpção inválida, tente novamente...\n");
            }
        }
    }
}
