import java.util.Random;
import java.util.Scanner;

public class JogoDaForca {
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
    private String letrasCertas = "";
    private String letrasErradas = "";
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

            if (letrasCertas.contains(letra)) {
                System.out.println("Você já tentou essa letra.");
                continue;
            }

            if (letrasErradas.contains(letra)) {
                System.out.println("Você já tentou essa letra e errou.");
                continue;
            }

            if (palavra.contains(letra)) {
                letrasCertas += letra;
                palavraOculta = ocultarLetras();
                System.out.println("Palavra: " + palavraOculta);

                if (palavraOculta.equals(palavra)) {
                    System.out.println("========================"
                            + "Parabéns! Você venceu."
                            + "========================");
                    break;
                }
            } else {
                letrasErradas += letra;
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
        for (int i = 0; i < tentativas; i++) {
            if (i < partesForca.length) {
                System.out.println(partesForca[i]);
            }
        }
        System.out.println("=============================\n");
    }

    private String ocultarLetras() {
        StringBuilder resultado = new StringBuilder();
        for (int i = 0; i < palavra.length(); i++) {
            char letra = palavra.charAt(i);
            if (letrasCertas.contains(String.valueOf(letra))) {
                resultado.append(letra);
            } else {
                resultado.append("_");
            }
        }
        return resultado.toString();
    }
}
