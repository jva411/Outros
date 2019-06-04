import java.io.*;
import java.util.*;
import java.lang.StringBuilder;

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
        public String toString(){
            return new StringBuilder().append('{').append(estado).append(',').append(cidade).append(',').append(rua).append(',').append(numero).append('}').toString();
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
        public String toString(){
            return new StringBuilder().append('{').append(nome).append(',').append(idade).append(',').append(endereco.toString()).append('}').toString();
        }
    }

    public static void main(String[] args) throws IOException{

        Pessoa p = new Pessoa("Gustavo", 18, new Endereco("Ceará", "Fortaleza", "573", 175));
        File file = new File("asd.txt");
        if(!file.exists()) file.createNewFile();
        ArrayList<Pessoa> pessoas = new ArrayList<>();
        pessoas.add(p);
        for(int i=0;i<50;i++) pessoas.add(new Pessoa("Fodase"+i, i, new Endereco("Fortaleza", "Motel Até Q' Fim", "347", 69)));
        toByte(pessoas, new FileOutputStream(file));
        pessoas = fromByte(new FileInputStream(file));
        for(Pessoa P:pessoas) System.out.println(P.toString());
    }

    public static void toByte(Object obj, OutputStream os){
        try{
            ObjectOutputStream oos = new ObjectOutputStream(os);
            oos.writeObject(obj);
            oos.writeUTF("\n");
            oos.flush();
            oos.close();
        }catch(IOException ex){
            ex.printStackTrace();
        }
    }

    public static ArrayList<Pessoa> fromByte(InputStream is){
        try{
            ObjectInputStream ois = new ObjectInputStream(is);
            ArrayList<Pessoa> p = (ArrayList<Pessoa>)ois.readObject();
            ois.close();
            return p;
        }catch(IOException | ClassNotFoundException ex){
            ex.printStackTrace();
            return null;
        }
    }

}