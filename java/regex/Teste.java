import java.io.*;

public class Teste{

    private static class Endereco implements Serializable{
        private String estado, cidade, rua;
        private int numero;
        public Endereco(String Estado, String Cidade, String Rua, int Numero){
            estado = Estado;
            cidade = Cidade;
            rua = Rua;
            numero = Numero;
        }
    }

    private static class Pessoa implements Serializable{
        private String nome;
        private int idade;
        private Endereco endereco;
        public Pessoa(String Nome, int Idade, Endereco Endereco){
            nome = Nome;
            idade = Idade;
            endereco = Endereco;
        }
    }

    public static void main(String[] args){

        Pessoa p = new Pessoa("Gustavo", 18, new Endereco("Ceará", "Fortaleza", "573", 175));
        toByte(p, System.out);
    }

    public static void toByte(Object obj, OutputStream os){
        try{
            ObjectOutputStream oos = new ObjectOutputStream(os);
            oos.writeObject(obj);
            oos.flush();
            oos.close();
        }catch(IOException ex){
            ex.printStackTrace();
        }
    }

    public static Pessoa fromByte(InputStream is){
        try{
            ObjectInputStream ois = new ObjectInputStream(is);
            Pessoa p = (Pessoa)ois.readObject();
            ois.close();
            return p;
        }catch(IOException ex){
            ex.printStackTrace();
            return null;
        }
    }

}